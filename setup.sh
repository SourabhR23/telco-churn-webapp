mkdir -p ~/.streamlit/

echo "\
[theme]\n\
primaryColor="#cbadba"\n\
backgroundColor="#173e43"\n\
secondaryBackgroundColor="#3fb0ac"\n\
textColor="#fae596"\n\
font="serif"\n\
" > ~/streamlit/config.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
