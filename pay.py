from alipay import AliPay
from alipay.utils import AliPayConfig

import qrcode,time

APPID = '9021000129661967'
app_private_key_string = open("Privatekey.txt").read()
alipay_public_key_string = open("alipayPublicCert.txt").read()


class pay:
    def __init__(self,out_trade_no,total_amount,timeout_express):
        self.out_trade_no = out_trade_no
        self.total_amount = total_amount
        self.subject = "Top up Balance for Biking Share"
        self.timeout_express = timeout_express


    def pay(self):
        alipay = AliPay(
            appid=APPID,
            app_notify_url=None,  # 默认回调 url
            app_private_key_string=app_private_key_string,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            alipay_public_key_string=alipay_public_key_string,
            sign_type="RSA2",  # RSA 或者 RSA2
            debug=True,  # 默认 False
            verbose=False,  # 输出调试数据
            config=AliPayConfig(timeout=15)  # 可选，请求超时时间
        )

        data = alipay.api_alipay_trade_precreate(
            subject= self.subject,
            out_trade_no=self.out_trade_no,
            total_amount= float(self.total_amount))

        #10000调用成功
        if data["code"] == "10000":
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=1
            )
            qr.add_data(data["qr_code"])  # 二维码所含信息
            img = qr.make_image()  # 生成二维码图片
            img.save('qrcode_image/qr_test_ali' + '_' + self.out_trade_no +'.png')
            print('二维码保存成功！')

        paid = False
        for i in range(100):
            # check every 3s, and 10 times in all
            print("now sleep 3s")
            time.sleep(3)
            result = alipay.api_alipay_trade_query(out_trade_no=self.out_trade_no)
            if result.get("trade_status", "") == "TRADE_SUCCESS":
                paid = True
                break
            print("not paid...")

        # order is not paid in 30s , cancel this order
        if paid is False:
            alipay.api_alipay_trade_cancel(out_trade_no= self.out_trade_no)

        return paid


if __name__ == '__main__':
  payer = pay("16","100.5","15m")
  flag = payer.pay()
  print(flag)