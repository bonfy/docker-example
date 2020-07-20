package main

import (
    "net/http"
    "encoding/json"
    "fmt"
)

// Resp Response VM
type Resp struct {
	Status string `json:"status"`
	Result string `json:"result"`
}


func main() {
    // Hello World
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        w.Write([]byte("Hello World"))
    })

    // Get Query
    http.HandleFunc("/query", func(w http.ResponseWriter, r *http.Request) {
        query := r.URL.Query()
        fmt.Printf(query.Encode())
        name := query.Get("name")
        fmt.Fprintf(w, "You input is: %s", name)
    })

    // Get Json
    http.HandleFunc("/getjson", func(w http.ResponseWriter, r *http.Request) {
        status := "ok"
        msg := "result"
        result := Resp{Status: status, Result: msg}
    
        // Case 1: Set header and w.Write
        js, err := json.Marshal(result)
        if err != nil {
        	http.Error(w, err.Error(), http.StatusInternalServerError)
        	return
        }
        w.Header().Set("Content-Type", "application/json")
        w.Write(js)
    })
    
    http.ListenAndServe("0.0.0.0:8888", nil)
}