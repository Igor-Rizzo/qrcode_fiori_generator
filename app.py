import qrcode

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2
)

qr.add_data('https://mobile.ourofino.com/sap/bc/ui5_ui5/ui2/ushell/shells/abap/FioriLaunchpad.html?sap-client=300&sap-language=PT')
qr.make(fit=True)

img = qr.make_image()
