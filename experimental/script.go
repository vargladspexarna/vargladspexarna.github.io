package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"
)

// This script will walk through a directory and build a JSON tree of the files
// Basically this can be used to convert the entirety of Spärmen into a lightweight JSON file usable by other programs.

func main() {
	root := os.Args[1]
	tree, err := buildTree(root)
	if err != nil {
		panic(err)
	}
	file, err := os.Create("output.json")
	if err != nil {
		panic(err)
	}
	defer func(file *os.File) {
		err := file.Close()
		if err != nil {
			panic(err)
		}
	}(file)
	jsonTree, err := json.MarshalIndent(tree, "", "  ")
	if err != nil {
		panic(err)
	}
	_, err = file.Write(jsonTree)
	if err != nil {
		panic(err)
	}
	fmt.Println("Output written to output.json")
}

func buildTree(root string) (interface{}, error) {
	tree := make(map[string]interface{})
	err := filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if info.IsDir() {
			return nil
		}
		relPath, err := filepath.Rel(root, path)
		if err != nil {
			return err
		}
		parts := strings.Split(relPath, string(filepath.Separator))
		node := tree
		for i, part := range parts[:len(parts)-1] {
			if _, ok := node[part]; !ok {
				node[part] = make(map[string]interface{})
				// Check if the current directory is a top-level directory or a second-level directory
				if i < 1 {
					// Split the directory name by underscore
					nameParts := strings.Split(part, "_")
					// Check if there was an underscore to split on
					if len(nameParts) > 1 {
						// Create a new map with the key `name` and the value as the directory name without the prefixed number
						meta := make(map[string]string)
						meta["number"] = nameParts[0]
						meta["name"] = strings.Join(nameParts[1:], "_")
						// Add this map to the `node` map under the key `meta`
						node[part].(map[string]interface{})["meta"] = meta

					}
				}
			}
			node = node[part].(map[string]interface{})
		}
		content, err := ioutil.ReadFile(path)
		if err != nil {
			return err
		}
		node[parts[len(parts)-1]] = string(content)
		return nil
	})
	if err != nil {
		return nil, err
	}
	return tree, nil
}