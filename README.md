# Building RPMSs

```sh
cd $pkgname
./docker.sh
```

In container:
```sh
cd /usr/local/$pkgname
./prepare.sh
```

Then all the RPMs will be available under `/root/rpmbuild/{RPMS,SRPMS}`.
