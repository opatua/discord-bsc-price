
# Discord Coins Price

This project is open-source use discord bot to monitor price from **CoinGecko**

# How To Use

> pip install -r requirements.txt

Available Django commands:
- Price `python manage.py discord_price_bot --channel_id=xxx --discord_bot_token=xxx --discord_bot_id=xxx --contract_address=0x4a8a99ac4e7973d20eb9e64db8eb94781dc80ba0 --network=binance-smart-chain`
- Volume `python manage.py discord_volume_bot --channel_id=xxx --discord_bot_token=xxx --discord_bot_id=xxx --contract_address=0x4a8a99ac4e7973d20eb9e64db8eb94781dc80ba0 --network=binance-smart-chain`
- Market cap `python manage.py discord_market_cap_bot --channel_id=xxx --discord_bot_token=xxx --discord_bot_id=xxx --contract_address=0x4a8a99ac4e7973d20eb9e64db8eb94781dc80ba0 --network=binance-smart-chain`
- Commands `python manage.py discord_command_bot --discord_bot_token=xxx`

Except from `commands` there's optional arguments `--target_currency=xxx` and  `--target_market=xxx`

> Options from `target_currency`= usd, btc, eth

> Example for `target_market`= pancakeswap, raydium
