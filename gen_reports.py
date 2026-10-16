# -*- coding: utf-8 -*-
"""生成国威/雄星/光裕三家公司调研报告 HTML"""
import os

OUT = r"C:\Users\29449\Documents\kimi\workspace\company-reports"

TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} · 调研报告</title>
<style>
  :root {{ --primary: {color}; --primary-dark: {color_dark}; --accent: #0e9f6e; --warn: #c81e1e;
    --bg: #f4f6fb; --card: #ffffff; --text: #1f2937; --muted: #6b7280; --border: #e5e7eb; }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: "Microsoft YaHei", "PingFang SC", "Segoe UI", sans-serif; background: var(--bg); color: var(--text); line-height: 1.75; padding: 32px 16px 64px; }}
  .container {{ max-width: 960px; margin: 0 auto; }}
  .hero {{ background: linear-gradient(135deg, {color_dark} 0%, {color} 60%, {color_light} 100%); color: #fff; border-radius: 16px; padding: 40px 36px; margin-bottom: 24px; box-shadow: 0 8px 24px rgba(0,0,0,.18); }}
  .hero .tag {{ display: inline-block; background: rgba(255,255,255,.18); border: 1px solid rgba(255,255,255,.35); font-size: 13px; padding: 3px 12px; border-radius: 999px; margin-bottom: 14px; }}
  .hero h1 {{ font-size: 28px; letter-spacing: 1px; margin-bottom: 8px; }}
  .hero .sub {{ font-size: 15px; opacity: .9; }}
  .hero .meta {{ margin-top: 18px; font-size: 13px; opacity: .8; }}
  .kpis {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(145px, 1fr)); gap: 14px; margin-bottom: 24px; }}
  .kpi {{ background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 16px 14px; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,.04); }}
  .kpi .v {{ font-size: 21px; font-weight: 700; color: var(--primary-dark); }}
  .kpi .l {{ font-size: 12px; color: var(--muted); margin-top: 4px; }}
  section {{ background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: 28px 30px; margin-bottom: 22px; box-shadow: 0 2px 8px rgba(0,0,0,.04); }}
  h2 {{ font-size: 20px; color: var(--primary-dark); padding-left: 12px; border-left: 4px solid var(--primary); margin-bottom: 18px; }}
  h3 {{ font-size: 16px; margin: 18px 0 10px; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 14px; margin: 10px 0 6px; }}
  th, td {{ border: 1px solid var(--border); padding: 9px 12px; text-align: left; vertical-align: top; }}
  th {{ background: {color_bg}; color: var(--primary-dark); font-weight: 600; white-space: nowrap; }}
  tr:nth-child(even) td {{ background: #fafbff; }}
  ul {{ padding-left: 22px; }} li {{ margin-bottom: 6px; }}
  .badge {{ display: inline-block; font-size: 12px; padding: 1px 9px; border-radius: 999px; margin-right: 6px; font-weight: 600; }}
  .badge-green {{ background: #def7ec; color: #03543f; }}
  .badge-blue {{ background: #e1effe; color: #1e429f; }}
  .badge-gray {{ background: #f3f4f6; color: #374151; }}
  .badge-amber {{ background: #fef3c7; color: #92400e; }}
  .badge-red {{ background: #fde8e8; color: #9b1c1c; }}
  .highlight {{ background: #fffbeb; border-left: 4px solid #f59e0b; padding: 12px 16px; border-radius: 0 8px 8px 0; margin: 12px 0; font-size: 14px; }}
  .risk {{ background: #fef2f2; border-left: 4px solid var(--warn); padding: 12px 16px; border-radius: 0 8px 8px 0; margin: 12px 0; font-size: 14px; }}
  .contact-box {{ background: {color_bg}; border: 1px dashed {color_light}; border-radius: 10px; padding: 16px 20px; font-size: 14px; margin: 10px 0; }}
  .contact-box b {{ color: var(--primary-dark); }}
  .src {{ font-size: 12px; color: var(--muted); margin-top: 14px; }}
  footer {{ text-align: center; font-size: 12px; color: var(--muted); margin-top: 28px; }}
  @media print {{ body {{ background: #fff; padding: 0; }} section, .hero, .kpi {{ box-shadow: none; }} }}
</style>
</head>
<body>
<div class="container">
  <div class="hero">
    <span class="tag">企业调研报告</span>
    <h1>{name}</h1>
    <div class="sub">{sub}</div>
    <div class="meta">调研日期：2026-10-16 ｜ 数据源：天眼查 · 前程无忧/BOSS直聘等公开招聘 · 公司官网及公开资料</div>
  </div>
  <div class="kpis">{kpis}</div>
  {sections}
  <footer>{footer}</footer>
</div>
</body>
</html>"""

def kpi(items):
    return "\n    ".join(f'<div class="kpi"><div class="v">{v}</div><div class="l">{l}</div></div>' for v, l in items)

def sec(title, body):
    return f'<section>\n    <h2>{title}</h2>\n    {body}\n  </section>'

COMPANIES = [
# ============ 国威 ============
{
 "file": "国威控股调研报告.html",
 "name": "广州国威控股集团有限公司",
 "sub": "国威文商旅控股集团 ｜ 裸眼 3D 沉浸式文旅「幻境空间」品牌 ｜ 曾用名：广州国威文商旅投资有限公司",
 "color": "#7c3aed", "color_dark": "#5b21b6", "color_light": "#a78bfa", "color_bg": "#f3e8ff",
 "kpis": kpi([
    ("1000 万", "注册资本"), ("2025-12", "工商登记/更名时间"), ("10 家", "控股子公司"),
    ("200+ 家", "宣称全球体验门店*"), ("273 项", "宣称知识产权*"), ("—", "社保人数未公示"),
 ]),
 "sections": "\n  ".join([
  sec("一、公司概况", """
    <table>
      <tr><th style="width:130px">公司名称</th><td>广州国威控股集团有限公司（曾用名：广州国威文商旅投资有限公司，对外宣传口径为"国威文商旅控股集团"）</td></tr>
      <tr><th>工商登记时间</th><td>2025-12-29（营销口径称集团创立于 2019 年，或为业务起始时间）</td></tr>
      <tr><th>注册资本</th><td>1,000 万人民币</td></tr>
      <tr><th>法定代表人</th><td>邓湛波（董事兼经理）</td></tr>
      <tr><th>注册地址</th><td>广州市番禺区钟村谢石公路 74 号 A 栋一楼 A102 房</td></tr>
      <tr><th>官网</th><td>未查到独立官网域名，网络形象以大量软文推广为主</td></tr>
      <tr><th>主营方向</th><td>裸眼 3D / 沉浸式数字体验设备与文旅项目（"幻境空间"悬空玻璃剧场、飞行剧场、轨道影院、球幕影院等），覆盖研发、内容制作、设备智造、场景建设与运营</td></tr>
      <tr><th>资质标签</th><td>工商标签仅"存续"（无高新/专精特新等公示标签）；宣称授权知识产权 273 项*</td></tr>
    </table>
    <div class="highlight">* 标注的"200+ 门店、36 亿曝光、273 项知识产权"等数字均来自其软文营销口径，无法通过权威渠道核验。</div>"""),
  sec("二、融资与上市", """
    <ul>
      <li><b>未上市、无公开融资记录</b>（天眼查融资历史为空）。</li>
    </ul>
    <h3>股东结构</h3>
    <table>
      <tr><th>股东</th><th>持股比例</th><th>认缴情况</th></tr>
      <tr><td>佛山市奕承投资有限公司</td><td>60%</td><td>600 万，2030 年缴付</td></tr>
      <tr><td>广州弘益产业发展有限公司</td><td>15%</td><td>150 万，2030 年缴付</td></tr>
      <tr><td>佛山丽波文化发展有限公司</td><td>15%</td><td>150 万，2030 年缴付</td></tr>
      <tr><td>郑州鼎睿文旅科技有限公司</td><td>10%</td><td>100 万，2030 年缴付</td></tr>
    </table>
    <div class="highlight">注意：全部股东认缴期限均在 2030 年，<b>实缴情况不明</b>；四名股东皆为法人股东，自然人实控人隐藏在背后，需进一步穿透。</div>"""),
  sec("三、经营情况：营收与利润", """
    <div class="highlight"><b>非上市企业，无公开财务数据</b>，工商年报财务项未公示，社保人数也未公示。</div>
    <ul>
      <li>可参考的间接信号：营销口径称"全球体验门店超 200 家、累计全网曝光 36 亿次、服务过千古情景区/北京朝阳合生汇/天津海博馆/南京科技馆等项目"——均来自软文，建议以合同、案例现场核实。</li>
    </ul>"""),
  sec("四、增长与扩张信号", """
    <h3>① 招聘 <span class="badge badge-red">无在招职位</span></h3>
    <ul><li>天眼查聚合的主流招聘平台上<b>未查到任何在招职位</b>——对于宣称"集团化运营、200+ 门店"的公司，这一信号偏弱。</li></ul>
    <h3>② 子公司布局 <span class="badge badge-green">扩张明显</span></h3>
    <ul><li>控股子公司 10 家，覆盖广州、北京、苏州、合肥、郑州/河南、深圳等地，多为 51%-100% 持股（详见关联公司表），全国布局动作真实存在。</li></ul>
    <h3>③ 行业影响力 <span class="badge badge-amber">软文驱动</span></h3>
    <ul>
      <li>2026 年在大众网、各地信息港等渠道密集投放"排行榜/推荐榜"软文（均为可购买的推广位，<b>非权威榜单</b>）；</li>
      <li>未见进入官方/权威机构榜单。</li>
    </ul>
    <h3>④ CEO 公开活动 <span class="badge badge-gray">低调</span></h3>
    <ul><li>法人邓湛波无公开报道、专访或行业活动记录。</li></ul>"""),
  sec("五、高管及联系方式", """
    <div class="contact-box">
      <b>联系电话：</b>15918584249（手机，来源：2025 年年报）<br>
      <b>营销热线：</b>19964049413（大量软文中出现的"集团联系电话"，大概率为销售/招商线）<br>
      <b>邮箱：</b>349264732@qq.com（2025 年报公示）<br>
      <b>地址：</b>广州市番禺区钟村谢石公路 74 号 A 栋一楼 A102 房
    </div>
    <h3>主要人员</h3>
    <table>
      <tr><th>姓名</th><th>职务</th></tr>
      <tr><td>邓湛波</td><td>董事、经理（法定代表人）</td></tr>
    </table>
    <div class="highlight"><b>HR 联系方式：</b>无公开直线，且该公司无在招职位、无公开招聘平台主页，HR 触达渠道不明；建议拨打 15918584249 或营销热线转接。<br>说明：工商公示仅含企业对外公开联系方式，不含高管个人手机号。</div>"""),
  sec("六、上下游及关联公司", """
    <h3>商业模式</h3>
    <p>面向景区、商业综合体、文博馆、科技馆提供沉浸式体验设备+内容+运营的一站式方案（To B/To G 项目制）。</p>
    <h3>上游（推测）</h3>
    <ul><li>LED/投影显示设备、伺服轨道、球幕、音响等硬件供应商；其旗下有"广州国威文娱设备制造有限公司"承担部分设备自产。</li></ul>
    <h3>下游客户（营销口径）</h3>
    <ul><li>千古情景区、张家口大境门、北京朝阳合生汇、天津海博馆、南京科技馆、西峡恐龙遗迹园等景区/商业体/文博馆。</li></ul>
    <h3>控股子公司（天眼查对外投资，10 家）</h3>
    <table>
      <tr><th>公司</th><th>持股</th><th>方向</th></tr>
      <tr><td>广州国威投资发展有限公司</td><td>100%</td><td>游乐设备销售、文艺创作</td></tr>
      <tr><td>北京国威盛世文化科技有限公司</td><td>90%</td><td>技术服务、人工智能平台</td></tr>
      <tr><td>苏州国之威文旅科技有限公司</td><td>85%</td><td>互联网信息服务、直播技术</td></tr>
      <tr><td>苏州国之威文化科技有限公司</td><td>81%</td><td>建设工程设计施工、节目制作</td></tr>
      <tr><td>广州国威文娱设备制造有限公司</td><td>80%</td><td>VR 设备、音响、可穿戴设备制造</td></tr>
      <tr><td>合肥盛世国威文旅有限公司</td><td>70%</td><td>VR 设备制造、工程研发</td></tr>
      <tr><td>广州宸远文化科技有限公司</td><td>60%</td><td>互联网销售、货物进出口</td></tr>
      <tr><td>北京盛世国威文化有限公司</td><td>51%</td><td>文艺创作、VR 设备</td></tr>
      <tr><td>国威（河南）文旅科技有限公司</td><td>51%</td><td>数字文化创意、电影摄制</td></tr>
      <tr><td>深圳盛世国威数字科技有限公司</td><td>51%</td><td>数字文化装备、软件开发</td></tr>
    </table>"""),
  sec("七、风险提示", """
    <div class="risk"><ol style="padding-left:20px">
      <li><b>工商登记时间短（2025-12-29）、注册资本仅 1,000 万</b>，与"全球化集团、200+ 门店"的宣传口径反差较大，合作前务必核实实体经营历史与实缴资本；</li>
      <li>股东全部为法人且认缴至 2030 年，实控人需穿透核查；</li>
      <li>无社保人数公示、无在招职位，组织规模真实性待验证；</li>
      <li>营销高度依赖可购买的软文"排行榜"，宣称数据（门店数、曝光量、知识产权数）均无权威佐证；</li>
      <li>财务完全不透明，建议项目合作采用分期付款+履约保障条款。</li>
    </ol></div>"""),
 ]),
 "footer": "数据来源：天眼查（工商信息-企业基本信息/主要人员/企业股东/对外投资，数据更新至 2026-10）｜ 大众网/速招猫等公开营销软文（营销口径已单独标注）<br>本报告基于公开信息整理，仅供商务参考，不构成投资建议。",
},
# ============ 雄星 ============
{
 "file": "雄星新材料调研报告.html",
 "name": "广东雄星新材料有限公司",
 "sub": "雄星控股集团旗下 ｜ PVC 压延薄膜制造（广告膜/地板膜/汽车装饰膜/医用包装膜）｜ 清远生产基地",
 "color": "#047857", "color_dark": "#065f46", "color_light": "#34d399", "color_bg": "#d1fae5",
 "kpis": kpi([
    ("3.68 亿", "注册资本"), ("2016 年", "成立（集团 1994 年创立）"), ("483 人", "社保人数"),
    ("25 亿", "集团年产值（官方口径）"), ("50+ 国", "出口市场"), ("20 个", "在招职位（扩张中）"),
 ]),
 "sections": "\n  ".join([
  sec("一、公司概况", """
    <table>
      <tr><th style="width:130px">公司名称</th><td>广东雄星新材料有限公司（雄星控股集团全资子公司，集团旗下还有广州市雄星塑料制品有限公司、广州市威联达增塑剂有限公司）</td></tr>
      <tr><th>成立日期</th><td>2016-03-04（集团创办于 1994 年 10 月）</td></tr>
      <tr><th>注册资本</th><td>36,800 万人民币（由 2.68 亿增资至 2.98 亿再增至 3.68 亿）</td></tr>
      <tr><th>法定代表人</th><td>许杰山（经理兼财务负责人）；执行董事为张锦辉（实控人）</td></tr>
      <tr><th>注册地址</th><td>清远市清城区源潭镇积余村（雄星产业园，厂区总面积近 380-730 亩）</td></tr>
      <tr><th>官网</th><td><a href="http://www.gdxxcl.com/" target="_blank">http://www.gdxxcl.com</a> ｜ 集团官网：<a href="https://www.gzxiongxing.com/" target="_blank">https://www.gzxiongxing.com</a></td></tr>
      <tr><th>主营产品</th><td>PVC 压延薄膜：超级透明膜、喷绘广告膜、商标膜、地板膜、道路警示膜、汽车车身改色膜、家居家电装饰膜、新型医用包装材料等</td></tr>
      <tr><th>资质</th><td><span class="badge badge-blue">高新技术企业</span><span class="badge badge-blue">专精特新中小企业</span><span class="badge badge-blue">科技型中小企业</span> 41 项专利、ISO/环境管理体系认证、SGS/ROHS 合规</td></tr>
      <tr><th>市场</th><td>出口美国、英国、德国、土耳其、印度、印尼、菲律宾等 50+ 国家；自称"全球 PVC 行业龙头"</td></tr>
    </table>"""),
  sec("二、融资与上市", """
    <ul><li><b>未上市、无外部融资记录</b>（天眼查融资历史为空），家族企业+集团控股架构。</li></ul>
    <h3>股东结构</h3>
    <table>
      <tr><th>股东</th><th>持股比例</th><th>说明</th></tr>
      <tr><td>广东雄星控股集团有限公司</td><td>约 60%（59.78%）</td><td>集团控股（部分实物出资）</td></tr>
      <tr><td>张锦辉</td><td>21.47%</td><td>实控人、执行董事</td></tr>
      <tr><td>张伟钊</td><td>18.75%</td><td>家族成员</td></tr>
    </table>"""),
  sec("三、经营情况：营收与利润", """
    <div class="highlight"><b>非上市企业，无公开财务数据。</b>可侧面参考：集团官方口径总年产值约 25 亿人民币（招聘/宣传资料），公司注册资本 3.68 亿、一二期总投资 12 亿，属重资产规模生产型企业。</div>
    <ul>
      <li>员工规模：社保 483 人（招聘信息称 400-500 人），集团整体 800+ 人；</li>
      <li>A 级纳税人（智联招聘×芝麻企业信用联合认证标注）。</li>
    </ul>"""),
  sec("四、增长与扩张信号", """
    <h3>① 招聘：持续放量 <span class="badge badge-green">扩张中</span></h3>
    <ul>
      <li>主流平台在招职位约 <b>20 个</b>，2025-06 至 2026-07 持续更新：普工、质检员 QC、配色/颜料技术员、仓管、机修、车工、水处理、会计/总账会计、工程监理、机械制图等生产配套岗位为主（4.5-9K），另有招商经理 9-15K（产业园招商）；</li>
      <li>薪资水平标注"全省同行前 40%"（智联×芝麻信用认证）。</li>
    </ul>
    <h3>② 产能扩张 <span class="badge badge-green">大手笔</span></h3>
    <ul>
      <li>二期 3.39 万㎡ 厂房（投资 2 亿）已完工投产；<b>三期 10 万㎡ 厂房（投资 3 亿）即将开工</b>；</li>
      <li>2020 年先后收购荣华（清远）柯式印刷、清远新恒粤陶瓷、清远科陶陶瓷，厂区总面积扩至近 730 亩；</li>
      <li>对外投资 3 家：清远鸿泰纸业（100%）、荣华（清远）柯式印刷（100%）、广东雄星纸业股份（70%）——向纸品/包装材料横向扩张。</li>
    </ul>
    <h3>③ 行业影响力 <span class="badge badge-amber">区域龙头</span></h3>
    <ul><li>自称"全球 PVC 行业龙头"（无第三方佐证）；职友集"清远新材料人气第 17 名"；高新技术企业+专精特新，行业地位为区域性规模龙头。</li></ul>
    <h3>④ CEO 公开活动 <span class="badge badge-gray">低调</span></h3>
    <ul><li>实控人张锦辉、法人许杰山均无公开报道或行业活动记录。</li></ul>"""),
  sec("五、高管及联系方式", """
    <div class="contact-box">
      <b>公司电话：</b>0763-3126868（座机，来源：2025 年年报）<br>
      <b>招聘热线（可触达 HR）：</b>0763-3293088<br>
      <b>HR 联系人：</b>张贝贝 13430243984（微信同号）｜ 陈女士 13553990839<br>
      <b>邮箱：</b>1098053531@qq.com（2025 年报公示）<br>
      <b>地址：</b>广东省清远市清城区源潭镇高桥雄星产业园
    </div>
    <h3>主要人员</h3>
    <table>
      <tr><th>姓名</th><th>职务</th><th>备注</th></tr>
      <tr><td>张锦辉</td><td>执行董事</td><td>实控人（直接+间接合计控制约 80%）</td></tr>
      <tr><td>许杰山</td><td>经理、财务负责人</td><td>法定代表人</td></tr>
      <tr><td>李腊勇</td><td>监事</td><td>—</td></tr>
    </table>
    <div class="highlight">说明：工商公示仅含企业对外公开联系方式；招聘联系人电话来自其官方招聘启事，可用于求职/合作对接。</div>"""),
  sec("六、上下游及关联公司", """
    <h3>商业模式</h3>
    <p>PVC 薄膜研发-生产-出口一体化制造商，集团内有增塑剂配套（威联达），产业链自闭环。</p>
    <h3>上游</h3>
    <ul><li>PVC 树脂、增塑剂（DOP/DINP/DOTP）、油墨等原料——集团关联方<b>广州市威联达增塑剂有限公司</b>自供增塑剂；设备以进口生产线为主。</li></ul>
    <h3>下游</h3>
    <ul><li>广告喷绘、地板/家居装饰、汽车改色贴膜、医用包装等行业客户，出口 50+ 国家（美国、英国、德国、土耳其、印度、东南亚等）。</li></ul>
    <h3>关联公司</h3>
    <table>
      <tr><th>主体</th><th>关系</th><th>说明</th></tr>
      <tr><td>广东雄星控股集团有限公司</td><td>控股股东（约 60%）</td><td>集团母公司，gzxiongxing.com</td></tr>
      <tr><td>广州市雄星塑料制品有限公司</td><td>集团兄弟公司</td><td>广州生产基地</td></tr>
      <tr><td>广州市威联达增塑剂有限公司</td><td>集团兄弟公司</td><td>上游增塑剂配套</td></tr>
      <tr><td>清远市鸿泰纸业有限公司</td><td>全资子公司</td><td>纸制品制造</td></tr>
      <tr><td>荣华（清远）柯式印刷有限公司</td><td>全资子公司（2020 收购）</td><td>包装印刷</td></tr>
      <tr><td>广东雄星纸业股份有限公司</td><td>控股 70%</td><td>纸制品+新型膜材料</td></tr>
    </table>"""),
  sec("七、风险提示", """
    <div class="risk"><ol style="padding-left:20px">
      <li>企知道显示存在<b>股权冻结等风险动态</b>（103 条相关动态）及司法案件标签，合作前建议查最新涉诉和股权状态；</li>
      <li>"全球 PVC 行业龙头""年产值 25 亿"为官方自述口径，无第三方审计数据佐证；</li>
      <li>重资产扩产（三期 3 亿）遇行业下行时折旧压力较大；</li>
      <li>出口占比高，受海外需求与汇率影响。</li>
    </ol></div>"""),
 ]),
 "footer": "数据来源：天眼查（工商信息/股东/对外投资/企业招聘，数据更新至 2026-10）｜ 前程无忧/BOSS直聘/清远人力资源网招聘启事（2025-05 至 2026-08）｜ 集团官网 gzxiongxing.com、百度百科、企知道<br>本报告基于公开信息整理，仅供商务参考，不构成投资建议。",
},
# ============ 光裕 ============
{
 "file": "光裕汽车空调调研报告.html",
 "name": "广州市光裕汽车空调制造有限公司",
 "sub": "汽车空调压缩机及配件制造商 ｜ 增城+惠州双工厂 ｜ 电动涡旋压缩机（新能源方向）",
 "color": "#c2410c", "color_dark": "#9a3412", "color_light": "#fb923c", "color_bg": "#ffedd5",
 "kpis": kpi([
    ("2006 年", "成立"), ("2,600 万", "注册资本"), ("233 人", "社保人数"),
    ("100 万台", "压缩机年产能（官网口径）"), ("27 项", "专利"), ("20 个", "在招职位（扩张中）"),
 ]),
 "sections": "\n  ".join([
  sec("一、公司概况", """
    <table>
      <tr><th style="width:130px">公司名称</th><td>广州市光裕汽车空调制造有限公司</td></tr>
      <tr><th>成立日期</th><td>2006-03-30</td></tr>
      <tr><th>注册资本</th><td>2,600 万人民币（实缴 2,600 万）</td></tr>
      <tr><th>法定代表人</th><td>王光美（执行董事兼经理，持股 99.96%）</td></tr>
      <tr><th>注册地址</th><td>广州市增城区正果镇正果大道 184 号（1 号工厂）；2 号工厂位于惠州市龙门县，占地 5 万㎡</td></tr>
      <tr><th>官网</th><td><a href="https://www.gzgyac.com" target="_blank">https://www.gzgyac.com</a></td></tr>
      <tr><th>主营产品</th><td>汽车空调压缩机（508/507 系列、电动涡旋压缩机）及配件、冷却系统；新能源电附件；模具制造</td></tr>
      <tr><th>资质</th><td><span class="badge badge-blue">高新技术企业</span><span class="badge badge-blue">省级专精特新</span><span class="badge badge-blue">创新型中小企业</span><span class="badge badge-gray">IATF16949</span><span class="badge badge-gray">ISO9001</span> 27 项专利（含发明专利）</td></tr>
      <tr><th>产能与设备</th><td>年产能 100 万台压缩机（官网口径）；从美、日、德引进数控加工中心、压铸设备、自动化装配线</td></tr>
    </table>"""),
  sec("二、融资与上市", """
    <ul><li><b>未上市、无外部融资记录</b>（天眼查融资历史为空），高度集中的家族股权：</li></ul>
    <table>
      <tr><th>股东</th><th>持股比例</th><th>认缴</th></tr>
      <tr><td>王光美</td><td>99.96%</td><td>2,599 万（2050 年缴付）</td></tr>
      <tr><td>王宇康</td><td>0.04%</td><td>1 万</td></tr>
    </table>"""),
  sec("三、经营情况：营收与利润", """
    <div class="highlight"><b>非上市企业，无公开财务数据</b>，年报财务项未公示。</div>
    <ul>
      <li>间接信号：社保 233 人（2024 年口径 197 人，近年有增长）；小微企业标签；</li>
      <li>产品同时供应国内外主机配套与售后市场（官网口径）。</li>
    </ul>"""),
  sec("四、增长与扩张信号", """
    <h3>① 招聘：两地同步扩张 <span class="badge badge-green">扩张中</span></h3>
    <ul>
      <li>主流平台在招约 <b>20 个职位</b>，2025-02 至 2026-06 持续更新；</li>
      <li><b>惠州龙门工厂岗位占比明显提升</b>（压铸领班 8K、压铸工艺员、设备维修工程师、机加品质主任等）——2 号工厂在扩产；</li>
      <li>广州岗：成本主管/专员、SQE、QE、CNC 工程师、模具设计、内贸/外贸业务员（俄语、阿拉伯语——中东/东欧市场方向）。</li>
    </ul>
    <h3>② 产能扩张</h3>
    <ul><li>2024 年 3 月获批建设自编号 A1 厂房（增正公路西侧），持续扩大生产规模；惠州 2 号工厂 5 万㎡ 已投产运营。</li></ul>
    <h3>③ 行业影响力 <span class="badge badge-amber">细分配套商</span></h3>
    <ul>
      <li>高新技术企业、省级专精特新、创新型中小企业；</li>
      <li>以展商身份参加"汽车热管理之家"等行业展会，主推<b>电动涡旋压缩机</b>（新能源车热管理方向）；未上权威排行榜。</li>
    </ul>
    <h3>④ CEO 公开活动 <span class="badge badge-gray">低调</span></h3>
    <ul><li>王光美无公开报道；对外曝光以展会参展为主。</li></ul>"""),
  sec("五、高管及联系方式", """
    <div class="contact-box">
      <b>公司电话：</b>020-82811788（座机，来源：2025 年年报）<br>
      <b>业务手机：</b>13928922939（黄页登记联系人"刘经理"）<br>
      <b>邮箱：</b>gygz88@163.com ｜ zhicai.wang@gzgyac.com ｜ 1531033268@qq.com 等（2025 年报公示多个）<br>
      <b>官网：</b>https://www.gzgyac.com<br>
      <b>地址：</b>广州市增城区正果镇正果大道 184 号
    </div>
    <h3>主要人员</h3>
    <table>
      <tr><th>姓名</th><th>职务</th><th>备注</th></tr>
      <tr><td>王光美</td><td>执行董事、经理</td><td>法定代表人，持股 99.96%</td></tr>
      <tr><td>刘俊权</td><td>监事</td><td>—</td></tr>
      <tr><td>王宇康</td><td>（股东）</td><td>持股 0.04%</td></tr>
    </table>
    <div class="highlight"><b>HR 联系方式：</b>无公开直线，公司在招"人事行政专员/助理"岗说明有专人负责招聘，建议拨打总机 020-82811788 转人事行政部。<br>说明：工商公示仅含企业对外公开联系方式，不含高管个人手机号。</div>"""),
  sec("六、上下游及关联公司", """
    <h3>商业模式</h3>
    <p>汽车空调压缩机及配件制造商，前装配套 + 售后市场双轨，含模具压铸自制能力。</p>
    <h3>上游</h3>
    <ul><li>铝材/压铸坯料、五金件、电机/电控（电动涡旋压缩机用）、密封件等供应商；公司有自有模具与压铸车间（惠州），部分结构件自制。</li></ul>
    <h3>下游</h3>
    <ul><li>国内外整车厂/主机配套客户与汽车售后市场（官网口径"产品远销国内外主机和售后市场"）；电动涡旋压缩机面向新能源车厂。</li></ul>
    <h3>关联公司</h3>
    <ul><li>天眼查对外投资记录为空，无控股子公司；股权结构单一（王光美 99.96%），未发现复杂关联网络。</li></ul>"""),
  sec("七、风险提示", """
    <div class="risk"><ol style="padding-left:20px">
      <li>财务不透明（非上市），合作前建议资信调查；</li>
      <li>注册资本 2,600 万、小微标签，规模在压缩机行业偏小，大单履约能力需实地考察；</li>
      <li>有司法案件标签（天眼查），建议核查具体涉诉内容；</li>
      <li>股权高度集中（99.96%），决策系于一人。</li>
    </ol></div>"""),
 ]),
 "footer": "数据来源：天眼查（工商信息/股东/企业招聘，数据更新至 2026-10）｜ 公司官网 gzgyac.com、汽车热管理之家展会资料、前程无忧/压铸人才网招聘页、百度百科<br>本报告基于公开信息整理，仅供商务参考，不构成投资建议。",
},
]

for c in COMPANIES:
    html = TEMPLATE.format(**c)
    with open(os.path.join(OUT, c["file"]), "w", encoding="utf-8") as f:
        f.write(html)
    print("generated:", c["file"], len(html), "bytes")
