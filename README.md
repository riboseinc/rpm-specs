# Ribose RPM Specs

## Building RPMSs

```sh
./docker.sh $pkgname
```

## Running the container and building manually

Enter the container:
```sh
./docker.sh
```

In container:
```sh
cd /usr/local/rpm-specs/$pkgname
./prepare.sh
```

Then all the RPMs will be available under `/root/rpmbuild/{RPMS,SRPMS}`.


## Automatically Building And Attempting Install

Append the following to your desired `$pkgname/prepare.sh` script:

```sh
yum install -y /root/rpmbuild/RPMS/x86_64/*.rpm
exec bash
```

Then run:

```sh
./docker.sh $pkgname
```

And you'll drop into a `bash` session once building / installing is
complete.
