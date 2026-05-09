import fitz


def extract(file):
	text = ""
	with fitz.open(file) as pdf:
		for page in pdf:
			text += str(page.get_text())
	return text


def search(query, ipc):
	query = query.lower()
	lines = ipc.split("\n")
	results = [line for line in lines if query in line.lower()]
	if results:
		return results[:15]
	return ["No relevant section found."]


def chatbot():
	print("Loading IPC document...")
	# adjust the path below to where your ipc.pdf is stored
	ipc = extract(r"ipc.pdf")
	while True:
		query = input("Ask a question about the IPC: ")
		if query.lower() == "exit":
			print("Goodbye!")
			break
		results = search(query, ipc)
		print("\n".join(results))
		print("-" * 50)


if __name__ == "__main__":
	chatbot()