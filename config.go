package main

import (
    "io/ioutil"
    "github.com/ghodss/yaml"
)

type Config struct {
    Sleeptime string `json:"sleeptime"`
}

func config() (sleeptime string){
    var v Config
    config_file, err := ioutil.ReadFile("/etc/gotosleep/config.yaml")
    check(err)
    yaml.Unmarshal(config_file, &v)
    sleeptime = v.Sleeptime
    return
}
