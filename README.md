# iot
 
## Prerequisites

you'll need:

-   Raspberry Pi OS GNU/Linux 11 (bullseye)
-   python3

## Getting Started

### Install dependencies
```shell
$ pip3 install selenium
```
```shell
$ sudo apt install chromium-chromedriver
$ which chromedriver
```

### Fix the port and launch browser(chromium)
```shell
$ sh ./launch_browser.sh
```

### Start real button trigger program
```shell
$ python3 switch_trigger.py
```
