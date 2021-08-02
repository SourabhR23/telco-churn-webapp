mkdir -p ~/.streamlit/

echo "[theme]
primaryColor="#cbadba"
backgroundColor="#173e43"
secondaryBackgroundColor="#3fb0ac"
textColor="#fae596"
font="serif"
[server]
port = $PORT
enableCORS = false
headless = true
\n\
" > ~/streamlit/config.toml