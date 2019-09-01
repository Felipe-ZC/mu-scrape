NAME=$([ $# -eq 0 ] && echo 'test' || echo $1) 
DIR=$([ $# -le 1 ] && echo 'test_results' || echo $2)
(rm ${DIR}/${NAME}.json || echo `No file named ${NAME}.json found`) && scrapy crawl news -o ${DIR}/${NAME}.json
js-beautify ${DIR}/${NAME}.json > ${DIR}/${NAME}_pretty.json 
echo 
