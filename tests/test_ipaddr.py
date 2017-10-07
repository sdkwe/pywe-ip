# -*- coding: utf-8 -*-

from pywe_ip import WechatIP, wechat_ips

from local_wecfg_example import WECHAT


class TestIPAddrCommands(object):

    def test_wechat_ips(self):
        appid = WECHAT.get('JSAPI', {}).get('appID')
        appsecret = WECHAT.get('JSAPI', {}).get('appsecret')

        ipaddr = WechatIP(appid=appid, secret=appsecret)
        wechat_ips1 = ipaddr.wechat_ips()
        assert isinstance(wechat_ips1, dict)

        wechat_ips2 = wechat_ips(appid=appid, secret=appsecret)
        assert isinstance(wechat_ips2, dict)

        assert wechat_ips1 == wechat_ips2
