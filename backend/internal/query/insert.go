package query

import (
	"context"
	"encoding/json"
	"log"
	"net/http"

	"github.com/jackc/pgx/v5/pgxpool"
)

type Data struct {
	Value string `json:"value"`
	Time string `json:"time"`
}


func Insert(response http.ResponseWriter,request *http.Request,pool *pgxpool.Pool) {
	var data Data
	err := json.NewDecoder(request.Body).Decode(&data)
	if err != nil {
		log.Printf("Error decoding json :%v",err)
		return
	}

	_,err = pool.Exec(context.Background(),`INSERT INTO public.light_sensor 
											VALUES ($1,$2);`,data.Value,data.Time)
	if err != nil {
		log.Printf("Error inserting the user in database: %v",err)
		return
	}

	response.WriteHeader(http.StatusCreated)
}