# Enabling and disabling yota internet

## Dependencies

```bash
    sudo apt install firefox-geckodriver python3-pip
    pip3 install selenium fake_useragent python-dotenv
```

## Add alias to ~/.bashrc or if you have zsh then to ~/.zshrc

## Variables

Create an .env file in the script folder and add password=yourpassword

```bash
    tee -a .bashrc << EOF
    alias yota="pytho3 /path/to/script
    EOF
```

## Launch

### Raise to 1000р

```bash
    yota up
```

### Down to 450р

```bash
    yota down
```
