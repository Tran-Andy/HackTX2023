package query

import (
    "context"
    "log"
    "net/http"

    "github.com/jackc/pgx/v5/pgxpool"
)

func DeleteAll(response http.ResponseWriter,request *http.Request, pool *pgxpool.Pool) {
    _,err := pool.Exec(context.Background(),`DELETE FROM public.light_sensor;`)
    if err != nil {
        log.Printf("Error with delete query :%v",err)
        return
    }
    response.WriteHeader(http.StatusAccepted)
}