import requests

def get_charizard_data():
    # 直接向官方 API 網址發出請求 (唔需要 SDK)
    url = "https://api.pokemontcg.io/v2/cards?q=name:charizard&pageSize=5"
    
    print("🔍 正在繞過 SDK，直接向官方伺服器攞數據...")
    
    try:
        response = requests.get(url)
        # 檢查連線是否成功
        if response.status_code == 200:
            data = response.json()
            cards = data.get('data', [])
            
            print(f"✅ 成功找到 {len(cards)} 張噴火龍！\n")
            
            for i, card in enumerate(cards):
                name = card.get('name')
                set_name = card.get('set', {}).get('name')
                image = card.get('images', {}).get('small')
                # 攞埋美金市價 (如果有)
                market_price = card.get('tcgplayer', {}).get('prices', {}).get('holofoil', {}).get('market', "N/A")
                
                print(f"{i+1}. 名稱: {name}")
                print(f"   系列: {set_name}")
                print(f"   美金市價: ${market_price}")
                print(f"   圖片網址: {image}")
                print("-" * 40)
        else:
            print(f"❌ 連線失敗，狀態碼: {response.status_code}")
            
    except Exception as e:
        print(f"💥 發生意外錯誤: {e}")

if __name__ == "__main__":
    get_charizard_data()