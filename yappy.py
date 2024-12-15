# yap py skibidi rizz

import argparse
from subprocess import run as subprocess_run
from sys import exit as sys_exit



BRAINROT_0 = '''
try	hawk
except	tuah
finally	spit on that thang
return	its giving
-	fanum tax
+	rizz
print	yap!yaap
True	aura
False	cooked
def	bop
while	let him cook
import	glaze
from	lock in
class	skibidi
if	chat is this real
elif	yo chat
else	only in ohio
for	mewing
break	just put the fries in the bag bro
continue	edge
assert	sus
raise	crashout
in	diddy
is	low key
# and	fr
or	bet
not	cap
with	pookie
as	ahh
global	GOAT
nonlocal	motion
del	delulu
yield	pause
yield from	pause no diddy
None	NPC
pass	pluh
self	unc
range	huzz
>	sigma
<	beta
≥	sigma twin
≤	beta twin
==	twin
=	ong
# async	
# await	
open	mog
# read	
# write	
close	demure
# list	
# set	
# dict	
'''.strip()



BRAINROT_1: dict[str | tuple[str], str] = {
	v: line.split("\t")[0]
	for line in BRAINROT_0.split("\n")
	if line[0] != "#"
	for v in line.split("\t")[1].split("!")
}



BRAINROT_2: dict[str, str] = {
	k: v
	for key, v in BRAINROT_1.items()
	for k in (key if isinstance(key, tuple) else [key])
}



BRAINROT = dict(sorted(BRAINROT_2.items(), key=lambda kv: (-len(kv[0]), kv[0])))



def main():
	parser = argparse.ArgumentParser(
		description="This script be out here mogging Yappy into regular Python like a true Sigma coder—straight skibidi efficiency with no cringe, just pure updog energy. 🐍 💻",
		# conflict_handler="L rizz",
	)
	parser.add_argument(
		"input_file_path",
		nargs="?",
	)
	parser.add_argument(
		"-O",
		"--rizzmaxxing",
		type=int, # TODO: change to `str` (gyat, mewing, looksmaxxing, ...)?
		default=0,
		help="beta control that Level 100 gyatt optimization rizz-straight mogging the settings for max skibidi! 🛠️ 💻"
	)
	parser.add_argument(
		"-l",
		"--lore",
		action="store_true", # so default is false
		help="yap da lore"
	)
	args, unknownargs = parser.parse_known_args()
	if args.lore:
		print("Yappy lore:\n\n"+"\n".join(l for l in BRAINROT_0.splitlines() if l[0] != "#"))
		sys_exit(0)
	global ARGUMENTS
	ARGUMENTS = args

	if args.input_file_path is None:
		print("💀: L rizz giving no `input_file_path`.")
		sys_exit(0)
	with open(args.input_file_path, "r") as file:
		yappy_code = "".join(file.readlines())

	def gen_is_code_at(code: str) -> list[bool]:
		is_code_at: list[bool] = []
		prev_c = ""
		# prev_prev_c = ""
		# f_str_level = 0
		for (i, c) in enumerate(code):
			# if c in ('"', "'") and prev_c == "f":
			# 	f_str_level += 1
			is_code_now = is_code_at[-1] if len(is_code_at) > 0 else True
			# if is_code_now and c in ('"', "'") and prev_c != "\\":
			# 	is_code_now = False
			# if not is_code_now and c in ('"', "'") and prev_c != "\\":
			# 	is_code_now = True
			if c in ('"', "'") and prev_c != "\\":
				is_code_now = not is_code_now
			if not is_code_now and c == "{":
				is_code_now = True
			if is_code_now and c == "}":
				is_code_now = False
			is_code_at.append(is_code_now)
			# prev_prev_c = prev_c
			prev_c = c
		return is_code_at

	def print_colored(code: str):
		is_code_at = gen_is_code_at(code)
		for (i, c) in enumerate(code):
			if not is_code_at[i]:
				print("\033[0;31m", end="")
			print(c, end="")
			if not is_code_at[i]:
				print("\033[0m", end="")

	def find_sus(code: str) -> tuple[str, int] | None:
		is_code_at = gen_is_code_at(code)
		for k in BRAINROT:
			start_i = 0
			while (i:=code.find(k, start_i)) != -1:
				if is_code_at[i]:
					return k, i
				start_i = i + 1
		return None

	def replace_from(s: str, start: int, old: str, new: str, count: int = 1) -> str:
		return s[:start] + s[start:].replace(old, new, count)

	code: str = yappy_code
	while (ki := find_sus(code)) is not None:
		k, i = ki
		code = replace_from(code, i, k, BRAINROT[k])
		# print_colored(code)
		# print()

	# print(code)

	# ohio skibidi sigma rizz:
	# eval(code)
	# os.system(python + f" -c '{code}'")
	# python = sys.orig_argv[0]

	# gyatt alpha aura:
	subprocess_run(["python", "-c", code, *unknownargs])





if __name__ == "__main__":
	main()

