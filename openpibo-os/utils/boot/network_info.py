import time

def disp(v):
  o.clear()
  o.set_font(size=12)
  eip = v[1] if v[0] == "" else v[0]
  wip = v[4] if v[2] == "" else v[2]
  ssid = v[5] if v[3] == "" else v[3]

  o.draw_text((0,0), "# NETWORK")
  o.draw_text((0,15), "[E]:{}".format(eip))
  o.draw_text((0,30), "[W]:{}".format(wip))
  o.draw_text((0,45), "[S]:{}".format(ssid))
  o.show()

if __name__ == "__main__":
  try:
    import subprocess
    from openpibo.oled import Oled

    o = Oled()
    o.set_font(size=20)

    for i in range(10):
      o.draw_text((7,20), "Ready... ({})".format(i+1))
      o.show()
      time.sleep(1)
      o.clear()
      time.sleep(0.5)

    data = subprocess.check_output(["/boot/get_network.sh"])
    data = data.decode('utf-8').strip('\n').split(',')
    disp(data)

  except Exception as ex:
    with open("/home/pi/boot_errmsg", "w") as f:
      f.write("[{}]\n{}".format(time.ctime(), ex))
