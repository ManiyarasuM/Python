
#value error
try: 
   a = int(input("No 1:"))
   b = int(input("No 2:"))
   c = int(input())
   print(d)
  # print(f"add = {a+b}")

except ValueError as e:
    print("Value Error",e)
except TypeError as e:
    print("Type Error",e)
except Exception:
    print("semthion your input wrong")
finally:
    print("Done!!")
