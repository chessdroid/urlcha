def hash_function(s):
	ans = 0
	p = 1121232123432123454321
	tmp = 1
	for t in s:
		ans+=ord(t)*tmp
		ans = ans % 10092003300140014003
		tmp = (tmp * p) % 10092003300140014003
	ans = ans % (62 ** 8)

	small_hash = ''

	for i in range(8):
		u = ans % 62
		ans = ans // 62
		if u < 26:
			small_hash = small_hash + chr(ord('a') + u)
		elif u < 36:
			small_hash = small_hash + chr(ord('0') + u - 26)
		else :
			small_hash = small_hash + chr(ord('A') + u - 36)
	return small_hash

print(hash_function("fkejqrhnbd"))


