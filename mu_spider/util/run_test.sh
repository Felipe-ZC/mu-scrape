BASE_DIR=/home/zubuddy/projects/mu_scrape/src/mu_spider #TODO: Make this an env var! (Maybe we can even use $(pwd)?)
SPIDER=$([ $# -eq 0 ] && echo subpop || echo $1) 
DIR=${BASE_DIR}/mu_spider/fout
FILE=${DIR}/${SPIDER}.jl

(rm ${FILE} || :) && scrapy crawl ${SPIDER} -a follow=True && vim ${FILE} 
#TODO: Why did ':%!python3 -m json.tool' work but not :%python3 -m json.tool'
#TODO: Only run this command if the -f option is passed in to script...
#TODO: Find out why this command messes up the encoding on FILE...
#-c ':%!python3 -m json.tool'
