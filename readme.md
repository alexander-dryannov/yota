# Enabling and disabling yota internet

## Dependencies

console```
    sudo apt install firefox-geckodriver python3-pip
    pip3 install selenium fake_useragent python-dotenv
```

## Add alias to ~/.bashrc or if you have zsh then to ~/.zshrc

console```
    tee -a ~/.bashrc << EOF
    alias yota="pytho3 /path/to/script
    EOF
```

## Variables

Create an .env file in the script folder and add password=yourpassword

## Launch

### Raise to 1000р

console```
    yota up
```

### Down to 450р

console```
    yota down
```
