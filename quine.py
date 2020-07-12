s = 's=%r;print(s%%s)'
print(s % s)

t = 'this is it'
s = 't=input()or t;print(f"t={repr(t)};s={repr(s)};exec(s)#{t}")'
exec(s)
