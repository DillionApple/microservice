package main
import "net/http"
import "fmt"

func main() {
    resp, _ := http.Get("http://127.0.0.1:8085/")
    fmt.Println(resp)
}