from sys import argv

script, user_name = argv
prompt = f'{script}> '

print('>>>>> function types', repr(argv))

print(f"Hi {user_name}, i'm the {script} running.")

print(f"What do you like?")
likes = input(prompt)

print(f"So, {user_name}, you like {likes}")


print(f"""
Okay, so you like {likes}, just like me.
You are {user_name}. Good luck with that.
Nice!!
""")
