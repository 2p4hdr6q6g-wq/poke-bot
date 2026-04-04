import requests
from supabase import create_client

# --- 1. 設定你的 Supabase ---
SUPABASE_URL = "https://xcjygoliiiaghsbrnmrs.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inhjanlnb2xpaWlhZ2hzYnJubXJzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUyMDgxMTEsImV4cCI6MjA5MDc4NDExMX0.N98DJPO_-bh0h-vRwoDnPNIj2le7ojI4VTdD0Om2tCs" # 記得填返你之前用開嗰條
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def add_to_my_collection(card_name_query, my_buy_price):
    # 2. 向官方 API 攞資料
    api_url = f"https://api.pokemontcg.io/v2/cards?q=name:{card_name_query}&pageSize=1"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        card_data = response.json().get('data', [])[0] # 攞第一張最準嘅
        
        # 提取資料
        name = card_data.get('name')
        set_name = card_data.get('set', {}).get('name')
        image = card_data.get('images', {}).get('small')
        # 攞美金市場價
        market_usd = card_data.get('tcgplayer', {}).get('prices', {}).get('holofoil', {}).get('market', 0)

        # 3. 準備入庫數據
        my_card = {
            "card_name": name,
            "set_name": set_name,
            "image_url": image,
            "purchase_price_hkd": my_buy_price, # 你輸入嘅買入價
            "current_market_usd": market_usd
        }

        # 4. 存入 Supabase
        supabase.table("my_collection").insert(my_card).execute()
        print(f"✨ 成功將【{name}】加入收藏！")
        print(f"💰 買入價: ${my_buy_price} | 目前美金市價: ${market_usd}")
    else:
        print("❌ 搵唔到呢張卡。")

if __name__ == "__main__":
    # 測試：假設你用 $1500 買咗張噴火龍
    add_to_my_collection("charizard", 1500)
    add_to_my_collection("pikachu", 500)
