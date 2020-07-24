for GD32E230 on-board gd-link flash erase write check

1. openocd -f cmsis-dap.cfg -f stm32l0.cfg
in another terminal:
2. python openocd_erase_flash.py
3. python openocd_write_flash.py
4. python openocd_check_flash.py
