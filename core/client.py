import asyncio
import threading
import websockets
import requests
from PyQt5.QtCore import pyqtSignal, QObject

from core.packet import PacketData
from function.Algorithm import MSerial
from function.Misc import binary_to_hex, hex_to_bytearray, decimal_to_8hex


class WebSocketThread(QObject):
    new_message = pyqtSignal(str)

    def __init__(self, uri):
        super().__init__()
        self.uri = uri
        self.loop = asyncio.new_event_loop()
        self.thread = threading.Thread(target=self._run_event_loop, daemon=True)
        self.websocket = None
        self.connected = False
        self.uid = None
        self.lastResult = 0
        self.heartbeat_interval = 5  # 心跳间隔，单位秒
        self.heartbeat_task = None  # 心跳任务

    # 更新序列号
    def update_result(self, PackData):
        _loc6_ = 0
        _loc7_ = 0
        while _loc7_ < len(PackData.byteBody):
            _loc6_ = (_loc6_ ^ PackData.byteBody[_loc7_] & 255)
            _loc7_ += 1
        self.lastResult = MSerial(self.lastResult, len(PackData.byteBody), _loc6_, int(PackData.cmdId, 16))

    # 构建发送心跳包task
    def start_heartbeat(self):
        if self.websocket is not None:
            # 创建发送心跳包异步任务
            self.heartbeat_task = asyncio.create_task(self.heartbeat())

    # 发送心跳包
    async def heartbeat(self):
        while self.websocket and self.websocket.open:
            await asyncio.sleep(self.heartbeat_interval)
            if self.uid is not None:
                try:
                    # 构造心跳包
                    SYSTEM_TIME = '0000001131000003ea' + self.uid + '00000000'
                    self.send_message(SYSTEM_TIME)
                except Exception as e:
                    print(f"Error sending heartbeat: {e}")
                    # 可以在这里处理连接丢失的情况，比如重新连接
                    break

    def _run_event_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self._connect_and_receive())

    async def _connect_and_receive(self):
        try:
            self.websocket = await websockets.connect(self.uri)
            self.connected = True
            print(f"连接到服务器{self.uri}")

            # 接收消息（这里使用无限循环）
            async for message in self.websocket:
                message = binary_to_hex(message)
                receivedPacket = PacketData(message[0:8], message[8:10], message[10:18], message[18:26], message[26:34],
                                            message[34:])
                if int(receivedPacket.cmdId, 16) == 1001:
                    self.lastResult = int(receivedPacket.result, 16)
                    self.start_heartbeat()
                if int(receivedPacket.cmdId, 16) == 1002:
                    SYSTEM_TIME_CHECK = '00000015310000a10c12312c6700000000' + receivedPacket.body
                    self.send_message(SYSTEM_TIME_CHECK)
                self.new_message.emit(f"Received|{int(receivedPacket.cmdId, 16)}|{receivedPacket.body}")
                # 根据需要处理消息

        except websockets.exceptions.ConnectionClosed:
            print("服务器关闭连接")
        except Exception as e:
            print(f"出现错误: {e}")
        finally:
            self.connected = False
            await self.websocket.close() if self.websocket is not None else None
            print("连接关闭")

    def send_message(self, message):
        asyncio.run_coroutine_threadsafe(self._send_message(message), self.loop)

    async def _send_message(self, message):
        if self.websocket is not None and self.websocket.open:
            # 构造发送包结构
            sendPacket = PacketData(message[0:8], message[8:10], message[10:18], message[18:26], message[26:34],
                                    message[34:])
            # 更新序列号
            self.update_result(sendPacket)
            sendPacket.userId=self.uid
            sendPacket.result = decimal_to_8hex(self.lastResult)
            # 发送数据
            await self.websocket.send(hex_to_bytearray(sendPacket.getPacket()))
            self.new_message.emit(f"Send|{int(sendPacket.cmdId,16)}|{sendPacket.body}")
        else:
            print("未连接服务器")

    def start(self):
        if not self.thread.is_alive():
            self.thread.start()
    def stop(self):
        pass

url = "https://seerh5login.61.com/online_gate"
try:
    response = requests.get(url)
    response.raise_for_status()  # 如果请求失败，抛出异常
    webSocketClient = WebSocketThread('ws://'+response.text)
    webSocketClient.start()
except requests.exceptions.RequestException as e:
    print(f"网络请求出现问题: {e}")

