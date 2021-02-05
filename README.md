# Clash_Gen_N

A simple tools to optimize clash subscribe link.

It is built for the new version of clash configuration(which means it does not support the legacy version).

It can IMPORT node settings from a upstream subscribe link, add your custom nodes and rules, then generate a new configuration file.

### Picture

![p0](https://github.com/cmd2001/Clash_Gen_N/blob/master/Pictures/p0.jpg)

### Settings

Change your settings in `config/config.py` and `config/custom_proxy.list`,

Customize your rules in `rules` by editing or adding new `.list` file and register new file in `config/config.py`.

(实在不行读代码，都来GitHub找项目了不可能这点代码都读不懂吧)

### Deployment

Use Apache2 on Debian 10 as example.

First, install apache2, python3, apache2-uwsgi.

```sh
sudo apt install apache2 python3 python3-pip libapache2-mod-uwsgi-py3
```

Then, install python3 extensions.

```sh
sudo pip3 install flask requests uwsgi pyyaml ruamel.yaml
```

Move Everything to `/var/www/clashGenN`, copy `app.conf` into `/etc/apache2/sites-available`, create a symbol link in `sites-enabled` by `sudo ln -s /etc/apache2/sites-available/app.conf /etc/apache2/sites-enabled/app.conf`.

Restart apache2 and enjoy it.

### Licenses

GPL v3.
