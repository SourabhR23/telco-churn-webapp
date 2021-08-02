mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
[theme]\n\
primaryColor="#cbadba"\n\
backgroundColor="#173e43"\n\
secondaryBackgroundColor="#3fb0ac"\n\
textColor="#fae596"\n\
font="serif"\n\
\n\
" > ~/streamlit/config.toml