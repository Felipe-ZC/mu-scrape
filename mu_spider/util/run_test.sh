#TODO: Handle case where DIR has a '/' at the end. 
#TODO: Improve arg parsing (getopt)

#TODO: Make this an env var!
BASE_DIR='/home/zubuddy/projects/mu_scrape/src/mu_spider'
SPIDER=$([ $# -eq 0 ] && echo subpop || echo $1) 
NAME=$([ $# -eq 1 ] && echo ${SPIDER}_test || echo $2) 
DIR=$([ $# -le 2 ] && echo ${BASE_DIR}/mu_spider/util/results || echo $3)
FILE=${DIR}/${NAME}.jl

(rm ${FILE} || echo `No file named ${NAME} found`) && scrapy crawl $1 -o ${FILE}
cat ${FILE}

printf '\nDone\n'\

#TODO: Why did ':%!python3 -m json.tool' work but not :%python3 -m json.tool'
#TODO: Only run this command if the -f option is passed in to script...
#TODO: Find out why this command messes up the encoding on FILE...
vim ${FILE} 
#-c ':%!python3 -m json.tool'
