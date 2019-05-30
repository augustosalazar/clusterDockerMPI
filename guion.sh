#!/bin/bash

docker stop dockeropenmpi_mpi_head_1
docker stop dockeropenmpi_mpi_node_1
docker stop dockeropenmpi_mpi_node_2
docker stop dockeropenmpi_mpi_node_3
docker stop dockeropenmpi_mpi_node_4
docker stop dockeropenmpi_mpi_node_5
docker stop dockeropenmpi_mpi_node_6

docker-compose build

docker-compose scale mpi_head=1 mpi_node=3