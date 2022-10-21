## Javagc and Sac Datasets
Javagc and sac datasets are two large for github to store online, so the two datasets are respectively separated into 20 parts using 

```shell
./sep.sh javagc
./sep.sh sac
```

To restore the original datasets, run

```shell
./combine.sh javagc
./combine.sh sac
```
