from icmp import redirect

a = redirect("192.168.1.106", "192.168.1.1")
a.setup()
a.sendPacket