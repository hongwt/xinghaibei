# 语音模块：处理语音识别和合成
import sys

# 尝试导入 pyttsx3，如果失败则使用模拟模式
try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("警告: 未安装 pyttsx3，语音合成将以文字输出代替。")

# 尝试导入 speech_recognition
try:
    import speech_recognition as sr
    ASR_AVAILABLE = True
except ImportError:
    ASR_AVAILABLE = False
    print("警告: 未安装 speech_recognition，语音识别将不可用。")

class VoiceAssistant:
    def __init__(self):
        self.engine = None
        if TTS_AVAILABLE:
            try:
                self.engine = pyttsx3.init()
                self.engine.setProperty('rate', 150)
            except Exception as e:
                print(f"语音引擎初始化失败: {e}")
                self.engine = None
        
    def speak(self, text):
        """
        文字转语音
        """
        print(f"[AI 说]: {text}")
        if self.engine:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except Exception:
                pass

    def listen(self):
        """
        语音转文字
        """
        if not ASR_AVAILABLE:
            print("[系统]: 语音识别库未安装，请使用键盘输入。")
            return None
            
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("[系统]: 请说话...")
            try:
                # 监听 5 秒超时
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                print("[系统]: 正在识别...")
                text = r.recognize_google(audio, language='zh-CN') # 需翻墙，或换用 recognize_sphinx (离线) / recognize_baidu
                print(f"[用户 说]: {text}")
                return text
            except sr.WaitTimeoutError:
                print("[系统]: 听不到声音")
                return None
            except sr.UnknownValueError:
                print("[系统]: 无法识别")
                return None
            except Exception as e:
                print(f"[系统]: 识别出错 {e}")
                return None

