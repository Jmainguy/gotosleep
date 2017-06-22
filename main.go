package main

import (
    "syscall"
    "time"
    "fmt"
)

func check(e error) {
    if e != nil {
        fmt.Println(e)
    }
}

func main() {

    // Endless loop, so it acts like a daemon
    for {
        t := time.Now()
        sleeptime := config()
        st := fmt.Sprintf(t.Format("15:04"))

        if st == sleeptime {
            fmt.Println("Shutting down")
            syscall.Reboot(syscall.LINUX_REBOOT_CMD_POWER_OFF)
        } else {
            fmt.Println("All good son")
            fmt.Printf("It is currently %s, and sleeptime is %s\n", st, sleeptime)
        }
        // Sleep for 30 seconds
        time.Sleep(30 * time.Second)
    }
}
