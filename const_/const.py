
ACCOUNT_SID = "AC129b5f94d84406f937302d53ab8b01d9"
AUTH_TOKEN = "8d831be37594549d552df18f2b9bc1e6"
EMAIL_USER_NAME = "serverroominform.ksu@gmail.com"
EMAIL_PASS_WORD = "seniorproject"
YEAR = "year"
MONTH ="month"
DATE = "date"
MINUTE = "minute"
SECOND = "second"
ALEART_TEMPLET = """

<table class="tg">
    <span style="border-collapse:collapse;border-spacing:0;">
      <tr>
        <th class="tg-jnas" colspan="5"><span style="font-weight:bold;font-size:16px;background-color:#fe0000;border-color:inherit;text-align:center;vertical-align:top" >Server Room {msg_type_cap} Alert </span></th>
      </tr>
      <tr>
        <td class="tg-p9hc" colspan="5" rowspan="4" ><span style="font-family:sans-serif; border-color:#000000;text-align:left;vertical-align:top">Hello Admin:<br>Critical temperature alert at:{time_str}<br>Temperature monitor shows that the current {msg_type} is {value} F.<br>Please check the server room condition immediately!</span></td>
      </tr>
      <tr>
      </tr>
      <tr>
      </tr>
      <tr>
      </tr>
      <tr>
        <td class="tg-p1dc" colspan="5" ><span style="font-family:cursive; border-color:inherit; text-align:left;vertical-align:top">message sent by:<br>Server Room Monitor</span></td>
      </tr>
    </span>
    </table>

"""

REPORT_TEMPLET = """

    <span style="border-collapse:collapse;border-spacing:0;">
    <table class="tg">
      <tr>
        <th class="tg-okmv" colspan="5"><span style="font-weight:bold;font-size:16px;background-color:#34ff34;border-color:inherit;text-align:center;vertical-align:top">Server Room Daily Report</span></th>
      </tr>
      <tr>
        <td class="tg-p9hc" colspan="5" rowspan="2"><span style="font-family:serif;border-color:#000000;text-align:left;vertical-align:top">Hello {user_name}<br><br>{welcome} Here is server room condition condition report from {start_time} to {end_time}.\
        </br>You will keep receiving report every day. To unsubscribe message notification, go to <a href="www.ksuserver.club/">Server Room Monitor Web Page</a>.</span></td>
      </tr>
      <tr>
      </tr>
      <tr>
        <td class="tg-p1dc" colspan="2">Tempreature</td>
        <td class="tg-0pky" rowspan="2"></td>
        <td class="tg-vfh4" colspan="2">Humidity</td>
      </tr>
      <tr>
        <td class="tg-p1dc" colspan="2">Average: {temp_avg}*F<br>Maximum: {temp_max}*F<br>Minimum: {temp_min}*F</td>
        <td class="tg-p1dc" colspan="2">Average: {humi_avg}%<br>Maximum: {humi_max}%<br>Minimum: {humi_min}%</td>
      </tr>
      <tr>
        <td class="tg-p1dc" colspan="5"><span style="font-family:cursive;border-color:inherit;text-align:left;vertical-align:top">Auto message sent by:<br><a href="www.ksuserver.club/">Server Room Monitor</a></span></td>
      </tr>
    </span>
    </table>

"""


TEMPERATURE = "temperature"
HUMIDITY = "humidity"
TIME = "time"
NAME = "name"
EMAIL = "email"
PHONE = "phone"