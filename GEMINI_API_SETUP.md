# 專題環境建置：申請你的 Gemini AI 實驗室門禁卡 (API Key)

嗨！在我們的專題中，我們會寫 Python 程式來呼叫 Google 的 Gemini AI 幫我們生成實驗用的題目。

為了讓程式能跟 Google 的伺服器溝通，你需要一把專屬的「門禁卡」——在程式領域，我們稱之為 **API Key（應用程式介面金鑰）**。這把鑰匙代表了你的身分，Google 看到這把鑰匙，才會同意幫你的程式運算。

**⚠️ 心理學實驗倫理與資安警告：** 這把 API Key 就像是你個人的信用卡密碼。**絕對不可以**把它直接寫在 Python 程式碼 (`.py` 檔) 裡面！如果你把程式碼傳給別人或上傳到網路，別人就可以盜用你的額度。我們稍後會教你如何安全地「隱藏」它。

---

## 第一階段：去 Google 申請你的門禁卡

1. **登入平台：** 打開瀏覽器，前往 [Google AI Studio 網站](https://aistudio.google.com/)。請用你常用的 Google 帳號登入（系統可能會跳出服務條款，請打勾同意）。
2. **尋找申請入口：** 進入主畫面後，請看畫面的**左側邊欄**，點擊一把小鑰匙圖案的 **「Get API key」**。
3. **建立金鑰：** 在畫面中間，點擊醒目的藍色按鈕 **「Create API key」**。
4. **選擇專案：** 系統會彈出一個視窗，請直接點擊 **「Create API key in a new project」** (在一個新專案中建立)。接著請耐心等待幾秒鐘，Google 正在後台幫你開通權限。
5. **複製並保管：** 畫面會彈出一串很長、由亂碼組成的字串（通常以 `AIza` 開頭）。這就是你的 API Key！**請立刻點擊旁邊的「Copy (複製)」按鈕**。
   * *注意：這個視窗一旦關閉，你就再也看不到這串密碼了。請先把它貼在電腦的記事本裡備用。*

---

## 第二階段：把門禁卡安全地放進專案中 (`.env` 檔)

為了安全，我們要把這串密碼放在一個獨立的、隱密的檔案中，讓 Python 自己去讀取。

1. **打開你的專案資料夾：** 打開你用來寫這次專題 Python 程式的那個資料夾（裡面應該會有助教給你的 `main.py` 等檔案）。
2. **建立隱藏檔案：** 在這個資料夾裡，新增一個純文字檔案，並將檔名命名為 **`.env`**（注意：前面有一個小數點，這代表這是一個隱藏的環境設定檔）。
3. **貼上金鑰：** 用筆記本（或 VS Code 等編輯器）打開這個 `.env` 檔案，在裡面輸入以下內容（等號右邊請貼上你剛剛複製的那一大串亂碼，**不要加任何引號或空格**）：
   ```text
   GEMINI_API_KEY=AIzaSy你的超級長密碼貼在這裡...

## 第三階段：安裝讀卡機並測試
現在你的資料夾裡有門禁卡(.env)了，我們需要教 Python 怎麼讀取它。

打開終端機 (Terminal)： 在你的程式編輯器（如 VS Code）中打開終端機。

安裝套件： 輸入以下指令，這會幫 Python 安裝讀取 .env 檔案的工具，以及 Google 的 AI 工具包：

```python
pip install python-dotenv google-generativeai
```

執行測試： 執行你的測試程式。如果畫面上成功印出 AI 的打招呼訊息，恭喜你，實驗環境建置大功告成！
```python
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
```
