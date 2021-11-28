// This is my very first golang program, I work in python basically.
package main

import(
    "fmt"
    // "strings"
    // "strconv"
	// "bufio"
	// "os"
)
var sum int=0
func sumofSquares(arr []int, i int,n int){
	if i<n{
		if arr[i]>0{
			sum +=(arr[i]*arr[i])
		}
		sumofSquares(arr,i+1,n)
		
	}
	
}
func takeArrayInputs(size int,i int, arr []int){
	if i<size{
		fmt.Scanf("%d",&arr[i])
		takeArrayInputs(size,i+1,arr)
	}
	
}
func Caseinput(n int){
	if n>0{
		var size int
		fmt.Scanf("%d",&size)
		arr := make([]int,size)
		takeArrayInputs(size,0,arr)
		sumofSquares(arr,0,size)
		fmt.Println(sum)
		sum = 0
		Caseinput(n-1)
	}
	
}
func main(){
    var n int
    fmt.Println("Enter the value of n: ")
    fmt.Scanf( "%d", &n)
	Caseinput(n)
}