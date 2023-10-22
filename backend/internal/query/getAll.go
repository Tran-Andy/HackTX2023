package query

import (
	"context"
	"encoding/json"
	"log"
	"net/http"

	"github.com/jackc/pgx/v5/pgxpool"
)

func GetAll(response http.ResponseWriter,request *http.Request,pool *pgxpool.Pool){
	response.Header().Set("Content-Type","application/json")

	var datas []Data

	row,err := pool.Query(context.Background(),`SELECT value,time
												FROM public.light_sensor;`)
	if err != nil {
		log.Printf("Error with the get query :%v", err)
		return
	}
	for row.Next() {
		var data Data
		err := row.Scan(&data.Value,&data.Time)
		if err != nil {
			log.Printf("Error scanning data :%v",err)
			return
		}
		datas = append(datas, data)
	}
	if err := row.Err(); err != nil {
		log.Printf("Error with the err :%v",err)
		return
	}

	jsonData,err := json.Marshal(datas)
	if err != nil {
		log.Printf("Error encoding json :%v",err)
		return
	}
	response.WriteHeader(http.StatusOK)
	response.Write(jsonData)
}