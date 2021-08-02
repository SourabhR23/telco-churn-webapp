mkdir -p ~/.streamlit/

echo "
[server]\n
headless = true\n
enableCORS=false\n
port = $PORT\n
[theme]\n
primaryColor="#020202"\n
backgroundColor="#173e43"\n
secondaryBackgroundColor="#3fb0ac"\n
textColor="#fae596"\n
font="serif"\n
" > ~/.streamlit/config.toml