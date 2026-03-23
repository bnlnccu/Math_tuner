import os
from dotenv import load_dotenv 
import google.generativeai as genai

print("系統初始化中...")

# 1. 讀取專案資料夾下的 .env 檔案
load_dotenv()

# 2. 從環境變數中抓取金鑰 (防呆檢查：確保學生有設定好)
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    print(" 錯誤：找不到 API Key！請檢查你是否有建立 .env 檔案，且內容格式正確。")
    exit()

# 3. 將金鑰交給 Google SDK
genai.configure(api_key=API_KEY)

# 4. 指定我們前面確認過有免費額度的 Flash 模型
model = genai.GenerativeModel('gemini-2.5-flash')

print("金鑰載入成功，正在嘗試呼叫 Gemini AI...")

# 5. 發送簡單的測試問題
try:
    prompt = "你好，我是正在進行專題的學生。請用一句話簡短地跟我打招呼，證明我成功連上你了。"
    response = model.generate_content(prompt)
    print("\nOK === 連線成功！AI 的回覆如下 === ")
    print(response.text)
except Exception as e:
    print("\nFAIL === 連線失敗！=== ")
    print(f"請檢查網路連線，或確認你的 API Key 是否複製完整。詳細錯誤：{e}")
