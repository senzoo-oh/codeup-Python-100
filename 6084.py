h, b, c, s = map(int,input().split())

memory_needed = h * b * c * s
memory_in_MB_needed = (((h * b * c * s)/8)/1024)/1024

print("%.1f MB" % memory_in_MB_needed)