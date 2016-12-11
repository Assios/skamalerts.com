#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from keys import MAILGUN_API_KEY

# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def send_multiple_mailgun(recipients, title, link, time, subject, img):
    for rec, token in recipients:
        html = generate_html(subject, title, link, time, rec, token, img)

        send_email_mailgun(rec, html)


def send_email_mailgun(rec, html, domain="skamalerts.com", api_key=MAILGUN_API_KEY):
    s = "alert"

    return requests.post(
        "https://api.mailgun.net/v3/" + domain + "/messages",
        auth=("api", api_key),
        data={"from": "SKAM ALERTS <" + s + "@" + domain + ">",
              "to": [rec],
              "subject": "Ny Skam-post!",
              "html": html})


def generate_welcome_mail(email, token):
    html = """\
  <!DOCTYPE html>
  <html>
  <head>
  <title>SKAM ALERTS</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <style type="text/css">
      /* CLIENT-SPECIFIC STYLES */
      body, table, td, a{-webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%;} /* Prevent WebKit and Windows mobile changing default text sizes */
      table, td{mso-table-lspace: 0pt; mso-table-rspace: 0pt;} /* Remove spacing between tables in Outlook 2007 and up */
      img{-ms-interpolation-mode: bicubic;} /* Allow smoother rendering of resized image in Internet Explorer */

      /* RESET STYLES */
      img{border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none;}
      table{border-collapse: collapse !important;}
      body{height: 100% !important; margin: 0 !important; padding: 0 !important; width: 100% !important;}

      /* iOS BLUE LINKS */
      a[x-apple-data-detectors] {
          color: inherit !important;
          text-decoration: none !important;
          font-size: inherit !important;
          font-family: inherit !important;
          font-weight: inherit !important;
          line-height: inherit !important;
      }

      /* MOBILE STYLES */
      @media screen and (max-width: 525px) {

          /* ALLOWS FOR FLUID TABLES */
          .wrapper {
            width: 100% !important;
              max-width: 100% !important;
          }

          /* ADJUSTS LAYOUT OF LOGO IMAGE */
          .logo img {
            margin: 0 auto !important;
          }

          /* USE THESE CLASSES TO HIDE CONTENT ON MOBILE */
          .mobile-hide {
            display: none !important;
          }

          .img-max {
            max-width: 100% !important;
            width: 100% !important;
            height: auto !important;
          }

          /* FULL-WIDTH TABLES */
          .responsive-table {
            width: 100% !important;
          }

          /* UTILITY CLASSES FOR ADJUSTING PADDING ON MOBILE */
          .padding {
            padding: 10px 5%\ 15px 5% !important;
          }

          .padding-meta {
            padding: 30px 5%\ 0px 5% !important;
            text-align: center;
          }

          .padding-copy {
               padding: 10px 5%\ 10px 5% !important;
            text-align: center;
          }

          .no-padding {
            padding: 0 !important;
          }

          .section-padding {
            padding: 50px 15px 50px 15px !important;
          }

          /* ADJUST BUTTONS ON MOBILE */
          .mobile-button-container {
              margin: 0 auto;
              width: 100% !important;
          }

          .mobile-button {
              padding: 15px !important;
              border: 0 !important;
              font-size: 16px !important;
              display: block !important;
          }

      }

      /* ANDROID CENTER FIX */
      div[style*="margin: 16px 0;"] { margin: 0 !important; }
  </style>
  </head>
  <body style="margin: 0 !important; padding: 0 !important;">

  <!-- HEADER -->
  <table border="0" cellpadding="0" cellspacing="0" width="100%">
      <tr>
          <td bgcolor="#ffffff" align="center">
              <!--[if (gte mso 9)|(IE)]>
              <table align="center" border="0" cellspacing="0" cellpadding="0" width="500">
              <tr>
              <td align="center" valign="top" width="500">
              <![endif]-->
              <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 500px;" class="wrapper">
                  <tr>
                      <td align="center" valign="top" style="padding: 15px 0;" class="logo">
                          <span style="font-size: 25px; color: #F2C12E;">skam</span><span style="font-size: 25px">alerts</span><span style="font-size: 25px; color: #F2A7AD;">.com</span>
                      </td>
                  </tr>
              </table>
              <!--[if (gte mso 9)|(IE)]>
              </td>
              </tr>
              </table>
              <![endif]-->
          </td>
      </tr>
      <tr>
          <td bgcolor="#132240" align="center" style="padding: 70px 15px 70px 15px;" class="section-padding">
              <!--[if (gte mso 9)|(IE)]>
              <table align="center" border="0" cellspacing="0" cellpadding="0" width="500">
              <tr>
              <td align="center" valign="top" width="500">
              <![endif]-->
              <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 500px;" class="responsive-table">
                  <tr>
                      <td>
                          <!-- HERO IMAGE -->
                          <table width="100%" border="0" cellspacing="0" cellpadding="0">
                              <tr>
                                    <td class="padding" align="center">
                                  </td>
                              </tr>
                              <tr>
                                  <td>
                                      <!-- COPY -->
                                      <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                          <tr>
                                              <td align="center" style="font-size: 25px; font-family: Helvetica, Arial, sans-serif; color: #F2C12E; padding-top: 30px;" class="padding">Velkommen!</td>
                                          </tr>
                                          <tr>
                                              <td align="center" style="padding: 20px 0 0 0; font-size: 16px; line-height: 25px; font-family: Helvetica, Arial, sans-serif; color: #d8d8d8;" class="padding">Takk for at du registrerte deg på <a href="http://skamalerts.com" style="color: #AAAAAA;">skamalerts.com</a>. Du vil motta epost-varslinger når det kommer nye Skam-innlegg på <a href="http://skam.p3.no" style="color: #AAAAAA;">skam.p3.no</a>.</td>
                                          </tr>
                                              <td align="center" style="padding: 20px 0 0 0; font-size: 16px; line-height: 25px; font-family: Helvetica, Arial, sans-serif; color: #d8d8d8;" class="padding">Hvis du vil ha gratis SMS-varsler når det kommer nye Skam-innlegg, kan du sende <b>SKAM</b> til <b>90 3000 95</b>.</td>
                                          <tr>
                                          </tr>
                                      </table>
                                  </td>
                              </tr>
                              <tr>
                                  <td align="center">
                                      <!-- BULLETPROOF BUTTON -->
                                      <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                          <tr>
                                              <td align="center" style="padding-top: 25px;" class="padding">
                                                  <table border="0" cellspacing="0" cellpadding="0" class="mobile-button-container">
                                                      <tr>
                                                      </tr>
                                                  </table>
                                              </td>
                                          </tr>
                                      </table>
                                  </td>
                              </tr>
                          </table>
                      </td>
                  </tr>
              </table>
              <!--[if (gte mso 9)|(IE)]>
              </td>
              </tr>
              </table>
              <![endif]-->
          </td>
      </tr>
      <tr>
          <td bgcolor="#ffffff" align="center" style="padding: 20px 0px;">
              <!--[if (gte mso 9)|(IE)]>
              <table align="center" border="0" cellspacing="0" cellpadding="0" width="500">
              <tr>
              <td align="center" valign="top" width="500">
              <![endif]-->
              <!-- UNSUBSCRIBE COPY -->
              <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center" style="max-width: 500px;" class="responsive-table">
                  <tr>
                      <td align="center" style="font-size: 12px; line-height: 18px; font-family: Helvetica, Arial, sans-serif; color:#666666;">
                          <span style="color:#F2A7AD;"><3</span>
                          <br>
                          <a href="https://skamalerts.com/unsubscribe?email=""" + email + """&token=""" + token + """" target="_blank" style="color: #666666; text-decoration: none;">Meld deg av</a>
                          <span style="font-family: Arial, sans-serif; font-size: 12px; color: #444444;">&nbsp;&nbsp;|&nbsp;&nbsp;</span>
                          <a href="https://skamalerts.com" target="_blank" style="color: #666666; text-decoration: none;">Besøk skamalerts.com</a>
                      </td>
                  </tr>
              </table>
              <!--[if (gte mso 9)|(IE)]>
              </td>
              </tr>
              </table>
              <![endif]-->
          </td>
      </tr>
  </table>

  </body>
  </html>
  """

    return html


def generate_html(subject, title, link, time, email, token, img):
    if title:
        title = ": " + title

    html = """\
  <!DOCTYPE html>
  <html>
  <head>
  <title>SKAM ALERTS</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <style type="text/css">
      /* CLIENT-SPECIFIC STYLES */
      body, table, td, a{-webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%;} /* Prevent WebKit and Windows mobile changing default text sizes */
      table, td{mso-table-lspace: 0pt; mso-table-rspace: 0pt;} /* Remove spacing between tables in Outlook 2007 and up */
      img{-ms-interpolation-mode: bicubic;} /* Allow smoother rendering of resized image in Internet Explorer */

      /* RESET STYLES */
      img{border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none;}
      table{border-collapse: collapse !important;}
      body{height: 100% !important; margin: 0 !important; padding: 0 !important; width: 100% !important;}

      /* iOS BLUE LINKS */
      a[x-apple-data-detectors] {
          color: inherit !important;
          text-decoration: none !important;
          font-size: inherit !important;
          font-family: inherit !important;
          font-weight: inherit !important;
          line-height: inherit !important;
      }

      /* MOBILE STYLES */
      @media screen and (max-width: 525px) {

          /* ALLOWS FOR FLUID TABLES */
          .wrapper {
            width: 100% !important;
              max-width: 100% !important;
          }

          /* ADJUSTS LAYOUT OF LOGO IMAGE */
          .logo img {
            margin: 0 auto !important;
          }

          /* USE THESE CLASSES TO HIDE CONTENT ON MOBILE */
          .mobile-hide {
            display: none !important;
          }

          .img-max {
            max-width: 100% !important;
            width: 100% !important;
            height: auto !important;
          }

          /* FULL-WIDTH TABLES */
          .responsive-table {
            width: 100% !important;
          }

          /* UTILITY CLASSES FOR ADJUSTING PADDING ON MOBILE */
          .padding {
            padding: 10px 5%\ 15px 5% !important;
          }

          .padding-meta {
            padding: 30px 5%\ 0px 5% !important;
            text-align: center;
          }

          .padding-copy {
               padding: 10px 5%\ 10px 5% !important;
            text-align: center;
          }

          .no-padding {
            padding: 0 !important;
          }

          .section-padding {
            padding: 50px 15px 50px 15px !important;
          }

          /* ADJUST BUTTONS ON MOBILE */
          .mobile-button-container {
              margin: 0 auto;
              width: 100% !important;
          }

          .mobile-button {
              padding: 15px !important;
              border: 0 !important;
              font-size: 16px !important;
              display: block !important;
          }

      }

      /* ANDROID CENTER FIX */
      div[style*="margin: 16px 0;"] { margin: 0 !important; }
  </style>
  </head>
  <body style="margin: 0 !important; padding: 0 !important;">

  <!-- HIDDEN PREHEADER TEXT -->
  <div style="display: none; font-size: 1px; color: #fefefe; line-height: 1px; font-family: Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;">
      Ei litta Skam-post har blitt publisert på skam.p3.no.
  </div>

  <!-- HEADER -->
  <table border="0" cellpadding="0" cellspacing="0" width="100%">
      <tr>
          <td bgcolor="#ffffff" align="center">
              <!--[if (gte mso 9)|(IE)]>
              <table align="center" border="0" cellspacing="0" cellpadding="0" width="500">
              <tr>
              <td align="center" valign="top" width="500">
              <![endif]-->
              <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 500px;" class="wrapper">
                  <tr>
                      <td align="center" valign="top" style="padding: 15px 0;" class="logo">
                          <span style="font-size: 25px; color: #F2C12E;">skam</span><span style="font-size: 25px">alerts</span><span style="font-size: 25px; color: #F2A7AD;">.com</span>
                      </td>
                  </tr>
              </table>
              <!--[if (gte mso 9)|(IE)]>
              </td>
              </tr>
              </table>
              <![endif]-->
          </td>
      </tr>
      <tr>
          <td bgcolor="#132240" align="center" style="padding: 70px 15px 70px 15px;" class="section-padding">
              <!--[if (gte mso 9)|(IE)]>
              <table align="center" border="0" cellspacing="0" cellpadding="0" width="500">
              <tr>
              <td align="center" valign="top" width="500">
              <![endif]-->
              <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 500px;" class="responsive-table">
                  <tr>
                      <td>
                          <!-- HERO IMAGE -->
                          <table width="100%" border="0" cellspacing="0" cellpadding="0">
                              <tr>
                                    <td class="padding" align="center">
                                  </td>
                              </tr>
                              <tr>
                                  <td>
                                      <!-- COPY -->
                                      <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                          <tr>
                                              <td align="center" style="font-size: 25px; font-family: Helvetica, Arial, sans-serif; color: #F2C12E; padding-top: 30px;" class="padding">Ny """ + subject + """<b>""" + title + """</b></td>
                                          </tr>
                                          <tr>
                                          """ + img + """
                                          </tr>
                                          <tr>
                                              <td align="center" style="padding: 20px 0 0 0; font-size: 16px; line-height: 25px; font-family: Helvetica, Arial, sans-serif; color: #d8d8d8;" class="padding">""" + time.capitalize() + """ ble det postet et nytt Skam-innlegg på <a href="http://skam.p3.no" style="color: #AAAAAA;">skam.p3.no</a>!</td>
                                          </tr>
                                          <tr>
                                              <td align="center" style="padding: 20px 0 0 0; font-size: 16px; line-height: 25px; font-family: Helvetica, Arial, sans-serif; color: #d8d8d8;" class="padding">Send SKAM til 90 3000 95 for å få gratis varsel på SMS!</td>
                                          </tr>
                                      </table>
                                  </td>
                              </tr>
                              <tr>
                                  <td align="center">
                                      <!-- BULLETPROOF BUTTON -->
                                      <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                          <tr>
                                              <td align="center" style="padding-top: 25px;" class="padding">
                                                  <table border="0" cellspacing="0" cellpadding="0" class="mobile-button-container">
                                                      <tr>
                                                          <td align="center" style="border-radius: 3px;" bgcolor="#256F9C"><a href=""" + link + """ target="_blank" style="font-size: 16px; font-family: Helvetica, Arial, sans-serif; color: #ffffff; text-decoration: none; color: #ffffff; text-decoration: none; border-radius: 3px; padding: 15px 25px; border: 1px solid #256F9C; display: inline-block;" class="mobile-button">Gå direkte til innlegget &rarr;</a></td>
                                                      </tr>
                                                  </table>
                                              </td>
                                          </tr>
                                      </table>
                                  </td>
                              </tr>
                          </table>
                      </td>
                  </tr>
              </table>
              <!--[if (gte mso 9)|(IE)]>
              </td>
              </tr>
              </table>
              <![endif]-->
          </td>
      </tr>
      <tr>
          <td bgcolor="#ffffff" align="center" style="padding: 20px 0px;">
              <!--[if (gte mso 9)|(IE)]>
              <table align="center" border="0" cellspacing="0" cellpadding="0" width="500">
              <tr>
              <td align="center" valign="top" width="500">
              <![endif]-->
              <!-- UNSUBSCRIBE COPY -->
              <table width="100%" border="0" cellspacing="0" cellpadding="0" align="center" style="max-width: 500px;" class="responsive-table">
                  <tr>
                      <td align="center" style="font-size: 12px; line-height: 18px; font-family: Helvetica, Arial, sans-serif; color:#666666;">
                          <span style="color:#F2A7AD;"><3</span>
                          <br>
                          <a href="https://skamalerts.com/unsubscribe?email=""" + email + """&token=""" + token + """" target="_blank" style="color: #666666; text-decoration: none;">Meld deg av</a>
                          <span style="font-family: Arial, sans-serif; font-size: 12px; color: #444444;">&nbsp;&nbsp;|&nbsp;&nbsp;</span>
                          <a href="https://skamalerts.com" target="_blank" style="color: #666666; text-decoration: none;">Besøk skamalerts.com</a>
                      </td>
                  </tr>
              </table>
              <!--[if (gte mso 9)|(IE)]>
              </td>
              </tr>
              </table>
              <![endif]-->
          </td>
      </tr>
  </table>

  </body>
  </html>
  """

    return html


def send_welcome_mail(email, token, domain="skamalerts.com", api_key=MAILGUN_API_KEY):
    s = "alert"
    html = generate_welcome_mail(email, token)

    return requests.post(
        "https://api.mailgun.net/v3/" + domain + "/messages",
        auth=("api", api_key),
        data={"from": "SKAM ALERTS <" + s + "@" + domain + ">",
              "to": email,
              "subject": "Velkommen til skamalerts.com!",
              "html": html})
