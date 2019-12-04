import requests
from bs4 import BeautifulSoup

latest_id = 27987
qty = 20

#generate list of puzzle IDs 
ids = range(latest_id - qty, latest_id)

for id in ids:
	try:
		#open url for puzzle
		url = "https://www.theguardian.com/crosswords/cryptic/" + str(id)
		print(url)
		user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
		headers = {'User-Agent': user_agent}
		puzzlepage = requests.get(url, headers=headers) 

		#extract pdf link
		puzzle = BeautifulSoup(puzzlepage.text, "html.parser")
		#print(puzzle)
		#pdf_link = puzzle.find("article", id="crossword").find_all("a").find_all("tr")
		#pdf_link = puzzle.find("article", id="crossword").find("PDF version").parent['href']
		#pdf_link = puzzle.find("article", id="crossword")#.find_all('a', href=True, text='PDF version')

		pdf_link = puzzle.find('a', href=True, text='PDF version')['href']

		print(pdf_link)

		#request pdf link
		puzzlepdf = requests.get(pdf_link)

		##save PDF link
		outfile = open(f'{id}.pdf', 'wb')
		outfile.write(puzzlepdf.content)
		outfile.close
	except:
		print(f"Error with {url}")
		pass
	
#from PyPDF2 import PdfFileMerger

#pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

#merger = PdfFileMerger()

#for pdf in pdfs:
#    merger.append(pdf)

#merger.write("result.pdf")
#merger.close()