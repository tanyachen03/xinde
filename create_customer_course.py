import os

BASE_DIR = '/workspace/data-analytics-platform'
COURSE_DIR = os.path.join(BASE_DIR, 'course', 'customer-advanced')

COURSE_DATA = {
    'title': '客户数据分析进阶',
    'subtitle': '成为数据驱动的分析指挥官',
    'modules': [
        {
            'id': 1,
            'name': '数据分析基本功',
            'icon': 'fa-database',
            'color': 'linear-gradient(135deg, #10b981, #34d399)',
            'lessons': [
                {
                    'id': 1,
                    'title': '数据觉醒：认识数据价值与思维转变',
                    'desc': '了解数据分析如何重塑商业决策，培养数据驱动思维',
                    'objectives': [
                        '理解数据资产的核心价值',
                        '区分描述性、诊断性、预测性分析',
                        '建立业务场景与数据指标的关联'
                    ],
                    'content': '''
                    <h3>数据时代的思维方式转变</h3>
                    <p>在传统商业决策中，管理者往往依靠经验和直觉。但在大数据时代，数据已经成为企业最重要的资产之一。数据驱动思维要求我们：用数据说话、用数据决策、用数据创新。</p>

                    <h3>数据分析的三个层次</h3>
                    <ul>
                        <li><strong>描述性分析（What）</strong>：发生了什么？如"上个月销售额下降了15%"</li>
                        <li><strong>诊断性分析（Why）</strong>：为什么发生？如"由于北方地区降雪，物流受阻导致订单延误"</li>
                        <li><strong>预测性分析（Future）</strong>：将要发生什么？如"基于历史趋势，下月销售额预计增长10%"</li>
                    </ul>

                    <h3>客户数据分析的关键指标</h3>
                    <p>在客户分析领域，我们需要关注以下核心指标：</p>
                    <ul>
                        <li><strong>客户获取成本（CAC）</strong>：获取一个新客户的平均成本</li>
                        <li><strong>客户生命周期价值（CLV）</strong>：客户在整个关系期内为企业带来的总价值</li>
                        <li><strong>客户留存率</strong>：在特定周期内继续使用产品/服务的客户比例</li>
                        <li><strong>NPS净推荐值</strong>：衡量客户推荐意愿的指标</li>
                    </ul>
                    ''',
                    'tips': '建立数据思维不是一蹴而就的，建议从每天分析一个业务问题开始，逐步培养数据敏感度。',
                    'errors': '常见错误：将数据当作万能答案，忽视业务理解和行业经验。数据只是决策的辅助工具。'
                },
                {
                    'id': 2,
                    'title': '数据清洗：面向客户数据的清洗实战',
                    'desc': '掌握客户数据的清洗方法，确保数据质量',
                    'objectives': [
                        '识别客户数据中的常见质量问题',
                        '掌握缺失值、异常值的处理方法',
                        '完成客户数据的标准化处理'
                    ],
                    'content': '''
                    <h3>客户数据常见质量问题</h3>
                    <p>客户数据通常存在以下问题：</p>
                    <ul>
                        <li><strong>缺失值</strong>：用户未填写完整信息，如手机号、邮箱等</li>
                        <li><strong>重复记录</strong>：同一客户被多次录入系统</li>
                        <li><strong>格式不统一</strong>：电话号码、日期等格式杂乱</li>
                        <li><strong>异常值</strong>：测试账号、刷单记录等干扰数据</li>
                    </ul>

                    <h3>代码示例：Pandas数据清洗实战</h3>
                    ''',
                    'code': '''import pandas as pd
import numpy as np

# 读取客户数据
df = pd.read_csv('customer_data.csv')

# 1. 处理缺失值
# 删除缺失率超过50%的列
threshold = len(df) * 0.5
df = df.dropna(axis=1, thresh=threshold)

# 用均值填充数值型缺失值
df['年龄'].fillna(df['年龄'].mean(), inplace=True)

# 用众数填充分类型缺失值
df['城市'].fillna(df['城市'].mode()[0], inplace=True)

# 2. 去除重复记录
df.drop_duplicates(subset=['手机号'], keep='first', inplace=True)

# 3. 数据类型标准化
df['手机号'] = df['手机号'].astype(str).str.replace(' ', '')
df['注册日期'] = pd.to_datetime(df['注册日期'])

# 4. 异常值检测（3σ原则）
z_scores = np.abs((df['消费金额'] - df['消费金额'].mean()) / df['消费金额'].std())
df = df[z_scores < 3]

print(f"清洗后数据量: {len(df)}")''',
                    'tips': '数据清洗是耗时最长的工作，但也是最重要的。业界有句话："垃圾进，垃圾出"——高质量的数据才能带来有价值的分析结果。',
                    'errors': '常见错误：直接删除所有缺失值，或用不合理的值（如0）填充，这会导致分析偏差。'
                },
                {
                    'id': 3,
                    'title': '客户画像与RFM分析：用户分层核心模型',
                    'desc': '构建客户标签体系，掌握RFM用户分层方法',
                    'objectives': [
                        '理解客户画像的概念和应用价值',
                        '掌握RFM模型的核心原理',
                        '能够独立完成RFM用户分层'
                    ],
                    'content': '''
                    <h3>什么是客户画像？</h3>
                    <p>客户画像（Customer Persona）是用标签化方式描述客户特征的技术。通过对客户人口统计、行为、偏好等维度的分析，形成具有代表性的客户原型。</p>

                    <h3>RFM模型详解</h3>
                    <p>RFM是客户价值分析中最经典的方法之一：</p>
                    <ul>
                        <li><strong>R（Recency）</strong>：最近一次消费距今时间，越近越有价值</li>
                        <li><strong>F（Frequency）</strong>：消费频率，越高越有价值</li>
                        <li><strong>M（Monetary）</strong>：消费金额，越高越有价值</li>
                    </ul>

                    <h3>代码示例：RFM分析实战</h3>
                    ''',
                    'code': '''import pandas as pd
import numpy as np
from datetime import datetime

# 计算RFM
def calculate_rfm(df, customer_id_col, order_date_col, amount_col):
    # 计算每个客户的RFM值
    rfm = df.groupby(customer_id_col).agg({
        order_date_col: lambda x: (datetime.now() - x.max()).days,
        customer_id_col: 'count',
        amount_col: 'sum'
    }).reset_index()

    rfm.columns = ['客户ID', 'R', 'F', 'M']

    # RFM打分（1-5分，5分最好）
    rfm['R_score'] = pd.qcut(rfm['R'], 5, labels=[5, 4, 3, 2, 1], duplicates='drop')
    rfm['F_score'] = pd.qcut(rfm['F'], 5, labels=[1, 2, 3, 4, 5], duplicates='drop')
    rfm['M_score'] = pd.qcut(rfm['M'], 5, labels=[1, 2, 3, 4, 5], duplicates='drop')

    # 用户分群
    def segment(row):
        if row['R_score'] >= 4 and row['F_score'] >= 4:
            return '重要价值客户'
        elif row['R_score'] >= 3 and row['F_score'] <= 2:
            return '重要发展客户'
        elif row['R_score'] <= 2 and row['F_score'] >= 3:
            return '重要保持客户'
        else:
            return '一般客户'

    rfm['用户分层'] = rfm.apply(segment, axis=1)
    return rfm

# 应用分析
rfm_result = calculate_rfm(orders_df, '客户ID', '下单日期', '消费金额')
print(rfm_result['用户分层'].value_counts())''',
                    'tips': 'RFM的分段阈值可以根据业务特点调整。比如奢侈品行业，F的重要性可能不如M；而快消品行业，F可能更重要。',
                    'errors': '常见错误：RFM三个维度权重相同。实际上不同行业这三个维度的重要性不同，需要结合业务调整。'
                },
                {
                    'id': 4,
                    'title': '数据可视化：商业图表与数据叙事基础',
                    'desc': '掌握商业可视化原则，让数据会说话',
                    'objectives': [
                        '理解不同图表的适用场景',
                        '掌握数据叙事的基本方法',
                        '能够制作清晰专业的商业图表'
                    ],
                    'content': '''
                    <h3>图表选择的黄金法则</h3>
                    <p>选择正确的图表是数据可视化的第一步：</p>
                    <ul>
                        <li><strong>趋势分析</strong>：折线图、时间序列图</li>
                        <li><strong>对比分析</strong>：柱状图、条形图</li>
                        <li><strong>占比分析</strong>：饼图、环形图、堆叠柱状图</li>
                        <li><strong>分布分析</strong>：直方图、箱线图、散点图</li>
                        <li><strong>关系分析</strong>：散点图、热力图</li>
                    </ul>

                    <h3>数据叙事的四步法</h3>
                    <ol>
                        <li><strong>背景设定</strong>：交代业务场景和数据来源</li>
                        <li><strong>问题提出</strong>：明确要解决的核心问题</li>
                        <li><strong>数据分析</strong>：用图表展示关键发现</li>
                        <li><strong>行动建议</strong>：基于数据提出具体建议</li>
                    </ol>

                    <h3>代码示例：商业仪表盘制作</h3>
                    ''',
                    'code': '''import matplotlib.pyplot as plt
import seaborn as sns

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 创建仪表盘
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('客户分析月度仪表盘', fontsize=16, fontweight='bold')

# 1. 客户增长趋势
axes[0, 0].plot(dates, new_customers, marker='o', color='#3b82f6')
axes[0, 0].set_title('新增客户趋势', fontsize=12)
axes[0, 0].set_ylabel('人数')
axes[0, 0].grid(True, alpha=0.3)

# 2. 客户来源分布
colors = ['#10b981', '#3b82f6', '#f59e0b', '#ef4444']
axes[0, 1].pie(source_counts, labels=source_labels, autopct='%1.1f%%', colors=colors)
axes[0, 1].set_title('客户来源占比', fontsize=12)

# 3. RFM分层柱状图
rfm_counts = rfm_result['用户分层'].value_counts()
axes[1, 0].bar(rfm_counts.index, rfm_counts.values, color=['#10b981', '#3b82f6', '#f59e0b', '#ef4444'])
axes[1, 0].set_title('RFM用户分层', fontsize=12)
axes[1, 0].tick_params(axis='x', rotation=15)

# 4. 留存率热力图
sns.heatmap(retention_matrix, annot=True, fmt='.0%', cmap='YlGnBu', ax=axes[1, 1])
axes[1, 1].set_title('客户留存率矩阵', fontsize=12)

plt.tight_layout()
plt.savefig('dashboard.png', dpi=150, bbox_inches='tight')
plt.show()''',
                    'tips': '好的可视化不是炫技，而是让观众一眼看懂。遵循"少即是多"原则，删除所有不必要的元素。',
                    'errors': '常见错误：在一个图表中展示太多数据系列；使用3D效果导致数据难以比较；颜色选择不当影响可读性。'
                }
            ]
        },
        {
            'id': 2,
            'name': '洞察客户行为',
            'icon': 'fa-users',
            'color': 'linear-gradient(135deg, #3b82f6, #60a5fa)',
            'lessons': [
                {
                    'id': 5,
                    'title': '客户细分：聚类分析与分层策略',
                    'desc': '运用聚类算法实现精细化客户分群',
                    'objectives': [
                        '理解K-Means聚类的原理',
                        '掌握客户聚类的分析流程',
                        '能够根据聚类结果制定差异化策略'
                    ],
                    'content': '''
                    <h3>为什么要做客户细分？</h3>
                    <p>不是所有客户都同等重要。通过客户细分，我们可以：</p>
                    <ul>
                        <li>识别高价值客户，进行重点维护</li>
                        <li>发现潜力客户，制定培养策略</li>
                        <li>识别流失风险客户，提前干预</li>
                        <li>针对不同群体设计差异化营销</li>
                    </ul>

                    <h3>聚类分析的常用算法</h3>
                    <ul>
                        <li><strong>K-Means</strong>：最常用，适合球形簇，效率高</li>
                        <li><strong>DBSCAN</strong>：基于密度，可发现任意形状簇，无需指定K</li>
                        <li><strong>层次聚类</strong>：生成树状图，适合小数据集</li>
                        <li><strong>GMM</strong>：高斯混合模型，软聚类，输出概率</li>
                    </ul>

                    <h3>代码示例：K-Means客户聚类实战</h3>
                    ''',
                    'code': '''import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# 特征工程：构建客户特征矩阵
features = ['最近购买距今天数', '购买频次', '平均订单金额', '累计消费金额', '登录次数']
X = customer_df[features]

# 数据标准化（聚类算法对量纲敏感）
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 确定最优K值（肘部法则 + 轮廓系数）
inertias = []
silhouettes = []
K_range = range(2, 10)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)
    silhouettes.append(silhouette_score(X_scaled, kmeans.labels_))

# 选择K=4（根据业务需求调整）
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
customer_df['Cluster'] = kmeans.fit_predict(X_scaled)

# 分析各簇特征
cluster_summary = customer_df.groupby('Cluster')[features].mean().round(2)
print(cluster_summary)

# 命名各簇
cluster_names = {
    0: '高价值活跃客户',
    1: '潜力沉睡客户',
    2: '一般观望客户',
    3: '流失风险客户'
}
customer_df['客户类型'] = customer_df['Cluster'].map(cluster_names)''',
                    'tips': '聚类结果需要结合业务理解来解释。比如一个特征值都很低的簇，可能代表"新客户"或"流失客户"，需要根据业务场景命名。',
                    'errors': '常见错误：直接用原始数据进行聚类（未标准化）；K值选择只看数学指标，忽视业务可解释性。'
                },
                {
                    'id': 6,
                    'title': 'CLV分析：客户生命周期价值计算与应用',
                    'desc': '预测客户长期价值，指导资源配置决策',
                    'objectives': [
                        '理解CLV的概念和商业价值',
                        '掌握CLV的计算方法和模型',
                        '能够应用CLV进行客户价值评估'
                    ],
                    'content': '''
                    <h3>什么是客户生命周期价值（CLV）？</h3>
                    <p>CLV（Customer Lifetime Value）是指客户在整个生命周期内为企业带来的总收益。CLV分析帮助企业回答：</p>
                    <ul>
                        <li>应该投入多少成本获取一个新客户？</li>
                        <li>哪些客户值得重点维护？</li>
                        <li>不同获客渠道的ROI如何？</li>
                    </ul>

                    <h3>CLV计算的基本公式</h3>
                    <p><strong>简单CLV = 平均订单价值 × 购买频率 × 客户生命周期 × 利润率</strong></p>

                    <h3>代码示例：BG/NBD模型预测CLV</h3>
                    ''',
                    'code': '''import pandas as pd
import numpy as np
from datetime import datetime

# 计算历史CLV
def calculate_historical_clv(df, customer_id, amount, profit_margin=0.3):
    clv = df.groupby(customer_id)[amount].sum() * profit_margin
    return clv

# 预测未来CLV（简化模型）
def predict_future_clv(customer_df, months=12, discount_rate=0.1):
    results = []

    for _, customer in customer_df.iterrows():
        # 获取该客户的购买历史
        transactions = get_customer_transactions(customer['客户ID'])

        # 计算平均订单价值和购买频率
        avg_order_value = transactions['金额'].mean()
        purchase_frequency = len(transactions) / transactions['月份跨度'].iloc[0]

        # 计算流失概率（简化的生存分析）
        churn_prob = calculate_churn_probability(customer)

        # 预测未来CLV
        expected_orders = purchase_frequency * months * (1 - churn_prob)
        future_clv = avg_order_value * expected_orders * 0.3  # 利润率30%

        # 折现到现值
        discounted_clv = future_clv / (1 + discount_rate) ** (months / 12)

        results.append({
            '客户ID': customer['客户ID'],
            '历史CLV': customer['累计消费'] * 0.3,
            '预测CLV': discounted_clv,
            '总CLV': customer['累计消费'] * 0.3 + discounted_clv
        })

    return pd.DataFrame(results)

clv_result = predict_future_clv(customer_df)
print(clv_result.sort_values('总CLV', ascending=False).head(10))''',
                    'tips': 'CLV不是固定值，会随客户行为变化而改变。建议每季度重新计算一次，及时调整客户策略。',
                    'errors': '常见错误：用单一公式计算CLV，忽视客户流失概率；假设所有客户的生命周期相同。'
                },
                {
                    'id': 7,
                    'title': '流失预警：识别高流失风险用户',
                    'desc': '建立流失预警模型，实现主动客户运营',
                    'objectives': [
                        '理解客户流失的定义和衡量标准',
                        '掌握流失预警模型的构建方法',
                        '能够识别流失风险客户并采取干预措施'
                    ],
                    'content': '''
                    <h3>客户流失的分类</h3>
                    <ul>
                        <li><strong>主动流失</strong>：客户主动取消订阅或停止购买</li>
                        <li><strong>被动流失</strong>：客户因服务终止、账号失效等原因流失</li>
                        <li><strong>自然流失</strong>：客户自然消亡（去世、迁居等）</li>
                    </ul>

                    <h3>流失预警的关键信号</h3>
                    <ul>
                        <li>购买频率显著下降</li>
                        <li>客单价突然降低</li>
                        <li>售后咨询/投诉增加</li>
                        <li>登录频率骤降</li>
                        <li>从使用核心功能转向边缘功能</li>
                    </ul>

                    <h3>代码示例：流失预警模型</h3>
                    ''',
                    'code': '''import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

# 准备特征
def create_churn_features(df, observation_period=30, churn_period=30):
    features = []

    for customer_id in df['客户ID'].unique():
        customer_data = df[df['客户ID'] == customer_id]

        # 计算行为特征
        recent = customer_data.tail(observation_period)
        older = customer_data.head(-observation_period) if len(customer_data) > observation_period else pd.DataFrame()

        feature = {
            '客户ID': customer_id,
            '最近购买间隔': recent['购买日期'].diff().mean().days if len(recent) > 1 else 0,
            '最近90天购买频次': len(recent),
            '最近90天消费金额': recent['金额'].sum(),
            '购买频次变化率': (len(recent) / len(older)) - 1 if len(older) > 0 else 0,
            '客单价变化率': (recent['金额'].mean() / older['金额'].mean()) - 1 if len(older) > 0 and older['金额'].mean() > 0 else 0,
        }

        # 流失标签：未来30天无购买
        future_data = customer_data.tail(churn_period)
        feature['是否流失'] = 1 if len(future_data) == 0 else 0

        features.append(feature)

    return pd.DataFrame(features)

# 构建数据集
df_features = create_churn_features(orders_df)

# 划分训练集和测试集
X = df_features.drop(['客户ID', '是否流失'], axis=1)
y = df_features['是否流失']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# 识别高风险客户
high_risk = df_features[df_features['是否流失'] == 1].head(20)
print(f"高流失风险客户：{len(high_risk)}")''',
                    'tips': '流失预警不是一次性工作。建议建立监控仪表盘，实时追踪流失风险指标的变化趋势。',
                    'errors': '常见错误：将流失定义得过于宽泛或过于狭窄；只关注模型准确率忽视业务可解释性。'
                },
                {
                    'id': 8,
                    'title': 'A/B测试：科学验证运营策略',
                    'desc': '掌握A/B测试方法论，实现数据驱动决策',
                    'objectives': [
                        '理解A/B测试的核心原理',
                        '掌握实验设计的关键要素',
                        '能够正确分析A/B测试结果'
                    ],
                    'content': '''
                    <h3>为什么需要A/B测试？</h3>
                    <p>A/B测试是互联网产品优化的核心方法。通过对照实验，我们可以：</p>
                    <ul>
                        <li>排除主观判断，用数据证明假设</li>
                        <li>小范围试错，降低决策风险</li>
                        <li>持续迭代优化，提升业务指标</li>
                    </ul>

                    <h3>A/B测试的关键要素</h3>
                    <ul>
                        <li><strong>假设</strong>：明确要验证的假设（如"红色按钮会提高点击率"）</li>
                        <li><strong>指标</strong>：选择核心指标（CTR、CVR、ARPU等）</li>
                        <li><strong>样本量</strong>：根据最小样本量公式计算</li>
                        <li><strong>分流</strong>：确保实验组和对照组同质</li>
                        <li><strong>时长</strong>：覆盖完整的用户周期</li>
                    </ul>

                    <h3>代码示例：A/B测试结果分析</h3>
                    ''',
                    'code': '''import pandas as pd
import numpy as np
from scipy import stats

# A/B测试结果数据
ab_results = pd.DataFrame({
    '组别': ['对照组'] * 1000 + ['实验组'] * 1000,
    '转化': control_conversions + treatment_conversions,
    '曝光': [1] * 1000 + [1] * 1000
})

# 计算转化率
def calculate_conversion_rate(df, group):
    group_data = df[df['组别'] == group]
    return group_data['转化'].sum() / len(group_data)

control_rate = calculate_conversion_rate(ab_results, '对照组')
treatment_rate = calculate_conversion_rate(ab_results, '实验组')

print(f"对照组转化率: {control_rate:.4f} ({control_rate*100:.2f}%)")
print(f"实验组转化率: {treatment_rate:.4f} ({treatment_rate*100:.2f}%)")
print(f"相对提升: {(treatment_rate - control_rate) / control_rate * 100:.2f}%")

# 统计显著性检验
def ab_test_analysis(control, treatment, n_control, n_treatment, alpha=0.05):
    # Z检验
    p_pool = (control + treatment) / (n_control + n_treatment)
    se = np.sqrt(p_pool * (1 - p_pool) * (1/n_control + 1/n_treatment))
    z_stat = (treatment/n_treatment - control/n_control) / se

    # P值
    p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

    # 置信区间
    diff = treatment/n_treatment - control/n_control
    ci_lower = diff - 1.96 * se
    ci_upper = diff + 1.96 * se

    return {
        'z统计量': z_stat,
        'p值': p_value,
        '95%置信区间': (ci_lower, ci_upper),
        '统计显著': p_value < alpha
    }

result = ab_test_analysis(control_conversions, treatment_conversions, 1000, 1000)
print(f"\\n统计显著性: {'显著' if result['统计显著'] else '不显著'}")
print(f"置信区间: [{result['95%置信区间'][0]:.4f}, {result['95%置信区间'][1]:.4f}]")''',
                    'tips': 'A/B测试不是万能的。有些变化（如品牌重塑）需要更长时间才能看到效果，不适合用短期A/B测试。',
                    'errors': '常见错误：只看绝对值忽视统计显著性；测试时间太短；样本不平衡导致结论偏差。'
                }
            ]
        },
        {
            'id': 3,
            'name': '驱动业务增长',
            'icon': 'fa-rocket',
            'color': 'linear-gradient(135deg, #8b5cf6, #a78bfa)',
            'lessons': [
                {
                    'id': 9,
                    'title': '精准营销：基于分群的营销策略',
                    'desc': '利用客户洞察实现精准触达和高效转化',
                    'objectives': [
                        '理解精准营销的核心概念',
                        '掌握基于分群的营销策略设计',
                        '能够构建营销闭环并进行效果评估'
                    ],
                    'content': '''
                    <h3>精准营销vs泛营销</h3>
                    <p>传统泛营销的问题：</p>
                    <ul>
                        <li>营销资源浪费严重</li>
                        <li>用户反感，损害品牌形象</li>
                        <li>转化率低，获客成本高</li>
                    </ul>

                    <p>精准营销的优势：</p>
                    <ul>
                        <li>触达真正有需求的用户</li>
                        <li>个性化的内容和体验</li>
                        <li>更高的ROI和用户满意度</li>
                    </ul>

                    <h3>精准营销的常见策略</h3>
                    <ul>
                        <li><strong>新客获取</strong>：相似人群扩展、裂变活动</li>
                        <li><strong>活跃转化</strong>：个性化推荐、限时优惠</li>
                        <li><strong>沉睡唤醒</strong>：定向福利、专属召回</li>
                        <li><strong>流失挽回</strong>：VIP专属服务、流失预警干预</li>
                    </ul>

                    <h3>代码示例：营销自动化策略</h3>
                    ''',
                    'code': '''import pandas as pd
from datetime import datetime, timedelta

# 客户分群营销策略
def design_marketing_strategy(customer_df, rfm_result):
    strategies = []

    for customer_id in customer_df['客户ID'].unique():
        customer = customer_df[customer_df['客户ID'] == customer_id].iloc[0]
        rfm = rfm_result[rfm_result['客户ID'] == customer_id].iloc[0]

        # 根据用户分层制定策略
        if rfm['R_score'] >= 4 and rfm['F_score'] >= 4:
            strategy = {
                '客户ID': customer_id,
                '分层': '高价值客户',
                '策略': '专属VIP服务，优先新品体验',
                '渠道': '1V1专属客服',
                '预期响应率': '85%'
            }
        elif rfm['R_score'] >= 3 and rfm['M_score'] >= 4:
            strategy = {
                '客户ID': customer_id,
                '分层': '潜力客户',
                '策略': '高客单价产品推荐，会员升级激励',
                '渠道': '短信+APP推送',
                '预期响应率': '45%'
            }
        elif rfm['R_score'] <= 2:
            strategy = {
                '客户ID': customer_id,
                '分层': '流失风险客户',
                '策略': '专属召回优惠，限时红包',
                '渠道': '电话+短信+邮件',
                '预期响应率': '25%'
            }
        else:
            strategy = {
                '客户ID': customer_id,
                '分层': '一般客户',
                '策略': '日常促销，新品推荐',
                '渠道': 'APP推送',
                '预期响应率': '15%'
            }

        strategies.append(strategy)

    return pd.DataFrame(strategies)

# 生成营销计划
marketing_plan = design_marketing_strategy(customer_df, rfm_result)
print(marketing_plan['策略'].value_counts())''',
                    'tips': '精准营销要把握好度。过度个性化可能让用户感到被监视；过于频繁的触达会造成骚扰。',
                    'errors': '常见错误：把精准营销等同于"大数据杀熟"；忽视用户隐私和体验。'
                },
                {
                    'id': 10,
                    'title': '全渠道体验：线上线下数据整合分析',
                    'desc': '打破数据孤岛，实现全渠道客户洞察',
                    'objectives': [
                        '理解全渠道数据整合的重要性',
                        '掌握多源数据融合的方法',
                        '能够构建统一的客户视图'
                    ],
                    'content': '''
                    <h3>什么是全渠道（Omni-Channel）？</h3>
                    <p>全渠道是指企业通过多种渠道（线上、线下、移动端、社交媒体等）与客户互动，并在所有渠道提供一致的品牌体验。核心目标是：</p>
                    <ul>
                        <li>打破渠道壁垒，实现数据互通</li>
                        <li>识别同一客户在不同渠道的行为</li>
                        <li>提供无缝衔接的跨渠道体验</li>
                    </ul>

                    <h3>全渠道数据整合的挑战</h3>
                    <ul>
                        <li><strong>数据格式不统一</strong>：各渠道数据结构差异大</li>
                        <li><strong>身份识别困难</strong>：难以关联同一用户的跨渠道行为</li>
                        <li><strong>数据质量问题</strong>：重复、缺失、不一致</li>
                    </ul>

                    <h3>代码示例：全渠道数据整合</h3>
                    ''',
                    'code': '''import pandas as pd
from datetime import datetime

# 模拟多渠道数据
online_orders = pd.DataFrame({
    '用户ID': ['U001', 'U001', 'U002'],
    '渠道': ['APP', '小程序', 'APP'],
    '行为': ['浏览', '下单', '支付'],
    '时间': ['2024-01-15 10:00', '2024-01-15 10:05', '2024-01-16 14:00']
})

offline_orders = pd.DataFrame({
    '会员手机': ['138****1234', '138****1234', '139****5678'],
    '门店': ['北京朝阳店', '北京海淀店', '上海浦东店'],
    '消费金额': [299, 599, 1299],
    '时间': ['2024-01-15 18:00', '2024-01-17 10:00', '2024-01-18 15:00']
})

# 用户身份匹配
# 线上用户绑定手机号
online_orders['手机'] = ['138****1234', '138****1234', '139****5678']

# 合并全渠道数据
all_channels = pd.concat([
    online_orders[['用户ID', '手机', '渠道', '时间']],
    offline_orders[['会员手机 as 手机', '门店 as 渠道', '时间']]
], ignore_index=True)

# 构建客户旅程视图
customer_journey = all_channels.sort_values(['手机', '时间'])
print(customer_journey)

# 计算各渠道贡献
channel_contribution = all_channels.groupby('渠道').agg({
    '手机': 'count',
}).rename(columns={'手机': '互动次数'})
print(channel_contribution)''',
                    'tips': '全渠道整合不是技术问题，而是组织问题。需要打破部门壁垒，建立统一的数据标准和治理机制。',
                    'errors': '常见错误：只关注数据整合技术，忽视业务流程再造；过度收集数据，侵犯用户隐私。'
                },
                {
                    'id': 11,
                    'title': '会员体系：积分与等级设计分析',
                    'desc': '设计科学的会员体系，驱动客户持续增长',
                    'objectives': [
                        '理解会员体系的核心价值和设计原则',
                        '掌握积分体系和等级设计的分析方法',
                        '能够评估会员体系效果并持续优化'
                    ],
                    'content': '''
                    <h3>会员体系的价值</h3>
                    <ul>
                        <li><strong>用户留存</strong>：积分和等级激励用户持续消费</li>
                        <li><strong>数据积累</strong>：会员数据支撑精细化运营</li>
                        <li><strong>品牌忠诚</strong>：差异化权益提升用户粘性</li>
                        <li><strong>成本可控</strong>：积分成本可量化预测</li>
                    </ul>

                    <h3>积分体系设计要点</h3>
                    <ul>
                        <li><strong>获取规则</strong>：消费返积分、行为积分、活动积分</li>
                        <li><strong>消耗规则</strong>：兑换礼品、抵扣现金、权益升级</li>
                        <li><strong>有效期</strong>：设置过期机制，促进及时消耗</li>
                        <li><strong>价值感</strong>：积分价值要让用户有感知</li>
                    </ul>

                    <h3>代码示例：会员等级价值分析</h3>
                    ''',
                    'code': '''import pandas as pd
import numpy as np

# 会员等级价值分析
def analyze_membership_value(member_df):
    # 按等级分组统计
    level_analysis = member_df.groupby('会员等级').agg({
        '客户ID': 'count',
        '累计消费': ['sum', 'mean'],
        '平均月消费': 'mean',
        '留存率': 'mean',
        '推荐率': 'mean'
    }).round(2)

    level_analysis.columns = ['会员数', '总GMV', '人均GMV', '月均消费', '留存率', '推荐率']

    # 计算会员ROI
    level_analysis['积分成本率'] = [0.02, 0.015, 0.01, 0.008]  # 假设各等级积分成本率
    level_analysis['积分成本'] = level_analysis['总GMV'] * level_analysis['积分成本率']
    level_analysis['边际收益'] = level_analysis['人均GMV'] - level_analysis['积分成本']

    # 边际效益分析
    level_analysis['边际效益比'] = (level_analysis['边际收益'] / level_analysis['积分成本']).round(2)

    return level_analysis

# 分析结果
value_report = analyze_membership_value(member_df)
print(value_report)

# 识别高价值等级
high_value_levels = value_report[value_report['边际效益比'] > 5].index.tolist()
print(f"\\n高效益等级: {high_value_levels}")''',
                    'tips': '会员体系要持续迭代。随着业务发展和用户变化，等级门槛和权益内容需要定期优化调整。',
                    'errors': '常见错误：积分通货膨胀，贬值严重；等级门槛设置不合理；权益同质化缺乏吸引力。'
                },
                {
                    'id': 12,
                    'title': '数据隐私：GDPR与合规数据分析',
                    'desc': '在保护隐私的前提下进行数据分析',
                    'objectives': [
                        '理解数据隐私保护的重要性',
                        '掌握GDPR等法规的核心要求',
                        '能够在合规框架下开展数据分析'
                    ],
                    'content': '''
                    <h3>为什么数据隐私越来越重要？</h3>
                    <p>近年来，全球数据隐私法规不断完善：</p>
                    <ul>
                        <li><strong>GDPR</strong>（欧盟通用数据保护条例）：最严格的隐私法规之一</li>
                        <li><strong>CCPA</strong>（加州消费者隐私法）：美国最全面的隐私法规</li>
                        <li><strong>PIPL</strong>（中国个人信息保护法）：中国版"GDPR"</li>
                    </ul>

                    <h3>法规核心原则</h3>
                    <ul>
                        <li><strong>合法正当</strong>：数据收集必须有合法依据</li>
                        <li><strong>目的明确</strong>：明确告知数据使用目的</li>
                        <li><strong>最小必要</strong>：只收集必要的个人信息</li>
                        <li><strong>用户授权</strong>：敏感数据需明确授权</li>
                        <li><strong>安全保障</strong>：采取必要技术措施保护数据</li>
                    </ul>

                    <h3>合规实践建议</h3>
                    ''',
                    'code': '''import pandas as pd

# 数据脱敏示例
def anonymize_customer_data(df):
    """
    符合隐私保护要求的数据处理流程
    """
    df_anonymized = df.copy()

    # 1. 直接标识符处理（删除或加密）
    df_anonymized['客户ID'] = df_anonymized['客户ID'].apply(lambda x: hashlib.md5(str(x).encode()).hexdigest()[:12])

    # 2. 准标识符泛化
    # 年龄泛化为年龄段
    df_anonymized['年龄段'] = pd.cut(df_anonymized['年龄'], bins=[0, 25, 35, 45, 55, 100], labels=['18-25', '26-35', '36-45', '46-55', '55+'])

    # 3. 敏感属性处理
    # 收入等级化
    df_anonymized['收入等级'] = pd.qcut(df_anonymized['收入'], q=5, labels=['极低', '较低', '中等', '较高', '极高'])

    # 4. 差分隐私添加噪声
    def add_laplace_noise(value, sensitivity, epsilon=1.0):
        noise = np.random.laplace(0, sensitivity / epsilon)
        return max(0, value + noise)

    # 对统计结果添加噪声
    df_anonymized['消费金额'] = df_anonymized['消费金额'].apply(lambda x: add_laplace_noise(x, sensitivity=1000))

    return df_anonymized

# 合规检查清单
compliance_checklist = [
    "数据收集是否获得用户明确授权？",
    "是否告知用户数据使用目的和范围？",
    "数据存储是否采取加密措施？",
    "是否建立数据访问权限管理？",
    "是否保留数据处理日志？",
    "是否制定数据泄露应急预案？",
    "用户是否可行使删除权？"
]
print("合规检查清单:", compliance_checklist)''',
                    'tips': '合规不是阻碍业务的障碍，而是建立用户信任的基础。将隐私保护融入产品设计，反而能成为竞争优势。',
                    'errors': '常见错误：认为合规只是法务的事；忽视员工的数据安全意识培训；数据脱敏不彻底导致泄露。'
                }
            ]
        },
        {
            'id': 4,
            'name': 'AI时代的分析指挥官',
            'icon': 'fa-robot',
            'color': 'linear-gradient(135deg, #f59e0b, #fbbf24)',
            'lessons': [
                {
                    'id': 13,
                    'title': 'AI时代的分析思维转型',
                    'desc': '拥抱AI工具，提升分析效率与洞察深度',
                    'objectives': [
                        '理解AI对数据分析工作的影响',
                        '掌握与AI协作的分析方法',
                        '能够利用AI工具提升工作效率'
                    ],
                    'content': '''
                    <h3>AI时代的分析工作变化</h3>
                    <p>AI正在深刻改变数据分析的工作方式：</p>
                    <ul>
                        <li><strong>自动化</strong>：数据清洗、可视化报告生成自动化</li>
                        <li><strong>智能化</strong>：预测模型、异常检测更加精准</li>
                        <li><strong>民主化</strong>：非技术人员也能进行自助分析</li>
                    </ul>

                    <h3>分析师的新定位</h3>
                    <p>AI不会取代分析师，但会用AI的分析师会取代不用AI的分析师。新的核心竞争力：</p>
                    <ul>
                        <li><strong>业务理解</strong>：深度理解业务场景和需求</li>
                        <li><strong>问题定义</strong>：将模糊的业务问题转化为可分析的问题</li>
                        <li><strong>AI协作</strong>：有效使用AI工具，评估AI输出质量</li>
                        <li><strong>沟通叙事</strong>：将复杂分析转化为业务语言</li>
                    </ul>

                    <h3>实用AI分析工具推荐</h3>
                    <ul>
                        <li><strong>ChatGPT/GPT-4</strong>：代码生成、数据解释、报告撰写</li>
                        <li><strong>GitHub Copilot</strong>：代码补全和分析脚本开发</li>
                        <li><strong>Tableau GPT</strong>：智能可视化分析</li>
                        <li><strong>Power BI Copilot</strong>：自然语言查询和报告生成</li>
                    </ul>

                    <h3>代码示例：AI辅助数据分析</h3>
                    ''',
                    'code': '''import pandas as pd
import openai

# 使用GPT进行数据洞察分析
def generate_data_insights(df, columns, api_key):
    """
    利用AI自动生成数据分析洞察
    """
    openai.api_key = api_key

    # 构建提示词
    data_summary = df[columns].describe().to_string()
    prompt = f"""
    请分析以下客户数据的特征，并给出3-5个关键洞察：

    数据统计摘要：
    {data_summary}

    请用业务语言解释这些数据的含义，并提出可操作的建议。
    """

    # 调用API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "你是一位资深数据分析师，擅长从数据中发现业务洞察。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message['content']

# 示例调用
# insights = generate_data_insights(customer_df, ['年龄', '消费金额', '购买频次'], OPENAI_API_KEY)
# print(insights)

# AI生成的SQL查询优化建议
def optimize_sql_with_ai(query, api_key):
    prompt = f"""
    请优化以下SQL查询，并解释优化点：

    {query}

    请给出优化后的SQL和性能提升建议。
    """
    # 调用AI进行SQL优化
    pass''',
                    'tips': 'AI是强大的助手，但不是完美的。始终保持批判性思维，验证AI的输出，才能真正发挥AI的价值。',
                    'errors': '常见错误：完全依赖AI，不加验证；不会提问，无法有效引导AI；忽视AI的伦理和偏见问题。'
                },
                {
                    'id': 14,
                    'title': '综合实战工作坊：完整项目演练',
                    'desc': '从需求到交付，完成端到端的数据分析项目',
                    'objectives': [
                        '掌握数据分析项目的完整流程',
                        '能够独立完成从需求到交付的全过程',
                        '积累完整的项目经验'
                    ],
                    'content': '''
                    <h3>数据分析项目标准流程</h3>
                    <ol>
                        <li><strong>业务理解</strong>：明确业务背景、目标、约束条件</li>
                        <li><strong>数据收集</strong>：获取相关数据源，了解数据结构</li>
                        <li><strong>数据探索</strong>：初步分析，理解数据质量</li>
                        <li><strong>数据清洗</strong>：处理缺失值、异常值、重复值</li>
                        <li><strong>特征工程</strong>：构建分析所需的特征</li>
                        <li><strong>建模分析</strong>：选择合适的模型和方法</li>
                        <li><strong>结果验证</strong>：检验分析结果的可靠性</li>
                        <li><strong>报告交付</strong>：形成可执行的业务建议</li>
                    </ol>

                    <h3>项目实战案例框架</h3>
                    ''',
                    'code': '''"""
客户流失分析与预警系统 - 完整项目
"""

# 1. 业务背景
"""
项目背景：
某电商平台近3个月用户流失率从8%上升至15%，
需要分析流失原因并建立预警系统。
"""

# 2. 数据收集
import pandas as pd
data_path = './data/customer_behavior.csv'
df = pd.read_csv(data_path)

# 3. 数据探索
print("数据概览:")
print(f"样本量: {len(df)}")
print(f"特征数: {df.shape[1]}")
print(df.info())

# 4. 特征工程
def create_features(df):
    features = pd.DataFrame()

    # 用户基本特征
    features['注册天数'] = (pd.Timestamp.now() - pd.to_datetime(df['注册日期'])).dt.days
    features['用户等级'] = df['会员等级'].map({'普通': 1, '银卡': 2, '金卡': 3, '钻石': 4})

    # 行为特征
    features['购买频次'] = df['订单数'] / (features['注册天数'] / 30 + 1)
    features['平均客单价'] = df['累计消费'] / (df['订单数'] + 1)
    features['活动参与率'] = df['参与活动数'] / (df['登录次数'] + 1)

    # 时序特征
    features['最近购买间隔'] = df['最后购买日期'].apply(
        lambda x: (pd.Timestamp.now() - pd.to_datetime(x)).days
    )
    features['最近登录间隔'] = df['最后登录日期'].apply(
        lambda x: (pd.Timestamp.now() - pd.to_datetime(x)).days
    )

    return features

# 5. 建模与评估
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score

X = create_features(df)
y = df['是否流失']

model = GradientBoostingClassifier(n_estimators=100)
cv_scores = cross_val_score(model, X, y, cv=5)
print(f"交叉验证准确率: {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")

# 6. 业务建议
"""
流失预警Top 3驱动因素:
1. 最近购买间隔 > 45天
2. 活动参与率 < 10%
3. 客单价下降 > 30%

建议策略:
- 对购买间隔超过30天的用户发送召回优惠券
- 提升活动个性化推荐精准度
- 关注客单价下降用户，进行1V1关怀
"""''',
                    'tips': '完成项目后，记得做复盘总结。好的复盘能让你从每个项目中获得成长。',
                    'errors': '常见错误：只关注技术实现，忽视业务理解；分析结果无法落地执行；项目文档不完整。'
                },
                {
                    'id': 15,
                    'title': '从数据到故事：数据叙事技巧',
                    'desc': '将复杂数据转化为有影响力的商业故事',
                    'objectives': [
                        '理解数据叙事的核心要素',
                        '掌握金字塔原理在分析报告中的应用',
                        '能够制作有说服力的数据汇报'
                    ],
                    'content': '''
                    <h3>为什么数据需要讲故事？</h3>
                    <p>数据本身不会说话。把数据变成故事，才能：</p>
                    <ul>
                        <li>吸引听众注意力</li>
                        <li>帮助理解复杂信息</li>
                        <li>推动决策和行动</li>
                        <li>加深记忆和影响</li>
                    </ul>

                    <h3>数据叙事的黄金公式</h3>
                    <p><strong>好故事 = 冲突 + 背景 + 解决 + 行动</strong></p>
                    <ul>
                        <li><strong>冲突</strong>：我们面临什么问题？（流失率上升15%）</li>
                        <li><strong>背景</strong>：这是怎么发生的？（用户行为分析）</li>
                        <li><strong>解决</strong>：我们发现了什么？（流失预警模型）</li>
                        <li><strong>行动</strong>：你应该做什么？（投入挽回计划）</li>
                    </ul>

                    <h3>数据叙事的五个技巧</h3>
                    <ol>
                        <li><strong>从一个关键洞察开始</strong>：开门见山，直击要害</li>
                        <li><strong>用类比降低理解门槛</strong>：用熟悉的事物解释陌生的概念</li>
                        <li><strong>让数字有温度</strong>：把"15%流失率"变成"每天流失100个客户"</li>
                        <li><strong>可视化要清晰</strong>：一张图只说一件事</li>
                        <li><strong>结尾要有行动号召</strong>：告诉观众下一步该做什么</li>
                    </ol>

                    <h3>数据叙事模板</h3>
                    ''',
                    'code': '''# 数据报告结构模板

"""
标题：直接点明核心发现
副标题：补充背景和来源

执行摘要（1段话）
- 核心发现
- 主要建议
- 预期收益

详细分析
1. 背景与目标
   - 业务背景
   - 分析目标
   - 数据来源

2. 关键发现
   发现1：...
   发现2：...
   发现3：...

3. 深度解读
   - 数据支撑
   - 原因分析
   - 影响评估

4. 行动建议
   建议1（高优先级）：...
   建议2（中优先级）：...
   建议3（低优先级）：...

5. 附录
   - 技术细节
   - 数据说明
   - 术语解释

"""

# 汇报PPT结构建议
slides = [
    {"title": "封面", "content": "项目名称 + 日期 + 汇报人"},
    {"title": "背景", "content": "为什么要做这个分析？"},
    {"title": "方法", "content": "我们是怎么做的？"},
    {"title": "发现1", "content": "最重要的发现"},
    {"title": "发现2", "content": "次要发现"},
    {"title": "建议", "content": "基于发现的行动建议"},
    {"title": "下一步", "content": "后续计划和时间表"},
    {"title": "Q&A", "content": "谢谢！"}
]''',
                    'tips': '练习数据叙事最好的方式是不断做汇报。每一次汇报都是一次提升的机会。',
                    'errors': '常见错误：堆砌数据，忽视主线；只讲技术细节，不讲业务价值；缺乏行动建议。'
                },
                {
                    'id': 16,
                    'title': '成果展示：制作专业分析报告',
                    'desc': '交付高质量的分析报告，展示专业能力',
                    'objectives': [
                        '掌握专业分析报告的写作规范',
                        '能够根据受众调整报告风格',
                        '积累可展示的项目作品集'
                    ],
                    'content': '''
                    <h3>分析报告的分类</h3>
                    <ul>
                        <li><strong>探索性报告</strong>：回答"发生了什么"，侧重描述性分析</li>
                        <li><strong>诊断性报告</strong>：回答"为什么发生"，侧重原因分析</li>
                        <li><strong>预测性报告</strong>：回答"将要发生什么"，侧重模型预测</li>
                        <li><strong>建议性报告</strong>：回答"应该怎么做"，侧重决策支持</li>
                    </ul>

                    <h3>专业报告的标准</h3>
                    <ul>
                        <li><strong>结构清晰</strong>：层次分明，逻辑通顺</li>
                        <li><strong>数据可靠</strong>：数据来源明确，质量有保障</li>
                        <li><strong>分析深入</strong>：透过现象看本质</li>
                        <li><strong>结论明确</strong>：直接回答业务问题</li>
                        <li><strong>可操作性</strong>：建议具体可执行</li>
                    </ul>

                    <h3>不同受众的报告风格</h3>
                    <ul>
                        <li><strong>高管</strong>：结论先行，数据简略，重视ROI</li>
                        <li><strong>业务负责人</strong>：方法论+数据+落地建议</li>
                        <li><strong>技术人员</strong>：详细方法论，代码和模型细节</li>
                    </ul>

                    <h3>分析报告模板</h3>
                    ''',
                    'code': '''# 专业分析报告模板

REPORT_TEMPLATE = """
# {项目名称}分析报告
**日期**: {日期}
**分析师**: {姓名}
**部门**: {部门}

---

## 执行摘要

{核心发现和关键建议，150字以内}

---

## 1. 项目背景

### 1.1 业务背景
{业务场景描述}

### 1.2 分析目标
- 目标1
- 目标2
- 目标3

### 1.3 数据说明
- 数据来源：{数据来源}
- 时间范围：{时间范围}
- 样本量：{样本量}

---

## 2. 分析方法

### 2.1 分析框架
{使用的分析方法论}

### 2.2 技术方案
{使用的工具和技术}

---

## 3. 关键发现

### 3.1 发现1
{发现描述}

**数据支撑**:
- 数据点1: {具体数字}
- 数据点2: {具体数字}

### 3.2 发现2
...

---

## 4. 行动建议

| 优先级 | 建议 | 预期收益 | 实施难度 |
|--------|------|----------|----------|
| P0 | 建议1 | XX万 | 低 |
| P1 | 建议2 | XX万 | 中 |

---

## 5. 风险与限制

{分析假设和局限性说明}

---

## 附录

### A. 数据字典
### B. 技术细节
### C. 参考资料

"""

# 生成报告示例
report = REPORT_TEMPLATE.format(
    项目名称="客户流失预警分析",
    日期="2024-01-20",
    姓名="张三",
    部门="数据分析部"
)
print(report)''',
                    'tips': '建立自己的报告模板库。每次完成报告后，总结好的表述方式，形成可复用的资产。',
                    'errors': '常见错误：报告太长，重点不突出；数据和结论脱节；忽视假设和局限性说明。'
                }
            ]
        }
    ]
}

# 项目数据
NEW_PROJECTS = [
    {'id': 'ab-test', 'name': 'A/B测试分析实战', 'difficulty': '中级', 'duration': '40分钟', 'desc': '设计并分析A/B测试'},
    {'id': 'churn-prediction', 'name': '客户流失预警实战', 'difficulty': '高级', 'duration': '50分钟', 'desc': '构建流失预警模型'},
    {'id': 'clv-prediction', 'name': '客户价值预测实战', 'difficulty': '高级', 'duration': '45分钟', 'desc': 'CLV预测模型构建'},
    {'id': 'marketing-strategy', 'name': '精准营销策略实战', 'difficulty': '中级', 'duration': '35分钟', 'desc': '分群营销策略设计'},
]

def create_course_page():
    """创建课程主页"""
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{COURSE_DATA['title']} - 数析学院</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="../styles.css">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        :root {{
            --primary: #1a1a2e;
            --primary-light: #16213e;
            --accent: #0f3460;
            --highlight: #e94560;
            --text-primary: #2d3436;
            --text-secondary: #636e72;
            --text-muted: #b2bec3;
            --bg-primary: #ffffff;
            --bg-secondary: #f8f9fa;
            --border: #e9ecef;
            --shadow-sm: 0 2px 8px rgba(0,0,0,0.04);
            --shadow-md: 0 4px 16px rgba(0,0,0,0.08);
            --shadow-lg: 0 8px 32px rgba(0,0,0,0.12);
            --radius-sm: 8px;
            --radius-md: 12px;
            --radius-lg: 16px;
        }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; line-height: 1.7; color: var(--text-primary); background: var(--bg-secondary); }}
        .navbar {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(255,255,255,0.95); backdrop-filter: blur(20px); border-bottom: 1px solid var(--border); }}
        .navbar-container {{ max-width: 1200px; margin: 0 auto; padding: 0 24px; height: 64px; display: flex; align-items: center; justify-content: space-between; }}
        .navbar-brand {{ display: flex; align-items: center; gap: 10px; font-size: 1.25rem; font-weight: 700; color: var(--primary); text-decoration: none; }}
        .navbar-brand i {{ color: var(--highlight); }}
        .navbar-menu {{ display: flex; gap: 32px; }}
        .navbar-link {{ font-size: 0.9375rem; font-weight: 500; color: var(--text-secondary); text-decoration: none; padding: 8px 0; position: relative; transition: all 0.3s; }}
        .navbar-link:hover, .navbar-link.active {{ color: var(--primary); }}
        .navbar-link::after {{ content: ''; position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background: var(--highlight); transition: all 0.3s; }}
        .navbar-link:hover::after, .navbar-link.active::after {{ width: 100%; }}
        .navbar-toggle {{ display: none; background: none; border: none; font-size: 1.5rem; color: var(--primary); cursor: pointer; }}
        .main-content {{ padding-top: 64px; }}
        .hero {{ background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%); color: white; padding: 80px 24px; text-align: center; position: relative; overflow: hidden; }}
        .hero::before {{ content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E"); opacity: 0.5; }}
        .hero-content {{ position: relative; z-index: 1; max-width: 800px; margin: 0 auto; }}
        .hero-badge {{ display: inline-flex; align-items: center; gap: 8px; background: rgba(233,69,96,0.2); border: 1px solid rgba(233,69,96,0.3); padding: 8px 16px; border-radius: 100px; font-size: 0.875rem; margin-bottom: 24px; }}
        .hero-badge i {{ color: var(--highlight); }}
        .hero h1 {{ font-size: 2.5rem; font-weight: 800; line-height: 1.2; margin-bottom: 16px; }}
        .hero-subtitle {{ font-size: 1.25rem; opacity: 0.9; margin-bottom: 32px; }}
        .section {{ padding: 60px 24px; }}
        .section-header {{ text-align: center; max-width: 600px; margin: 0 auto 40px; }}
        .section-tag {{ display: inline-block; font-size: 0.875rem; font-weight: 600; color: var(--highlight); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px; }}
        .section-title {{ font-size: 2rem; font-weight: 700; color: var(--primary); margin-bottom: 12px; }}
        .section-desc {{ font-size: 1.125rem; color: var(--text-secondary); }}
        .container {{ max-width: 1000px; margin: 0 auto; }}
        .modules-grid {{ display: flex; flex-direction: column; gap: 24px; }}
        .module-card {{ background: var(--bg-primary); border-radius: var(--radius-md); box-shadow: var(--shadow-md); overflow: hidden; }}
        .module-header {{ padding: 24px 28px; display: flex; align-items: center; justify-content: space-between; cursor: pointer; transition: background 0.2s; }}
        .module-header:hover {{ background: var(--bg-secondary); }}
        .module-info {{ display: flex; align-items: center; gap: 16px; }}
        .module-icon {{ width: 56px; height: 56px; border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center; }}
        .module-icon i {{ font-size: 1.5rem; color: white; }}
        .module-title h3 {{ font-size: 1.125rem; font-weight: 600; color: var(--text-primary); margin-bottom: 4px; }}
        .module-title p {{ font-size: 0.875rem; color: var(--text-secondary); }}
        .module-meta {{ display: flex; align-items: center; gap: 12px; }}
        .lesson-count {{ font-size: 0.875rem; color: var(--text-muted); background: var(--bg-secondary); padding: 6px 12px; border-radius: 100px; }}
        .expand-icon {{ font-size: 1.25rem; color: var(--text-muted); transition: transform 0.3s; }}
        .module-card.open .expand-icon {{ transform: rotate(180deg); }}
        .module-lessons {{ max-height: 0; overflow: hidden; transition: max-height 0.3s ease; }}
        .module-card.open .module-lessons {{ max-height: 2000px; }}
        .lesson-list {{ padding: 0 28px 24px; }}
        .lesson-item {{ display: flex; align-items: center; padding: 14px 16px; border-radius: var(--radius-sm); text-decoration: none; color: var(--text-primary); transition: all 0.2s; margin-bottom: 8px; background: var(--bg-secondary); }}
        .lesson-item:hover {{ background: rgba(233,69,96,0.08); transform: translateX(4px); border-left: 3px solid var(--highlight); }}
        .lesson-number {{ width: 32px; height: 32px; border-radius: 50%; background: white; display: flex; align-items: center; justify-content: center; font-size: 0.875rem; font-weight: 600; margin-right: 14px; color: var(--accent); }}
        .lesson-info {{ flex: 1; }}
        .lesson-info h4 {{ font-size: 0.95rem; font-weight: 600; margin-bottom: 2px; }}
        .lesson-info p {{ font-size: 0.8rem; color: var(--text-secondary); }}
        .lesson-arrow {{ color: var(--accent); }}
        .footer {{ background: var(--primary); color: white; padding: 48px 24px 24px; }}
        .footer-content {{ max-width: 1200px; margin: 0 auto; text-align: center; }}
        .footer p {{ opacity: 0.7; font-size: 0.875rem; }}
        @media (max-width: 768px) {{
            .navbar-menu {{ display: none; }}
            .navbar-toggle {{ display: block; }}
            .hero h1 {{ font-size: 1.75rem; }}
            .hero-subtitle {{ font-size: 1rem; }}
            .section {{ padding: 40px 16px; }}
            .module-header {{ padding: 16px 20px; flex-wrap: wrap; gap: 12px; }}
            .lesson-list {{ padding: 0 20px 16px; }}
        }}
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="navbar-container">
            <a href="../index.html" class="navbar-brand">
                <i class="fas fa-chart-line"></i>
                <span>数析学院</span>
            </a>
            <div class="navbar-menu">
                <a href="../index.html" class="navbar-link">首页</a>
                <a href="../course-center.html" class="navbar-link">课程中心</a>
                <a href="customer-advanced.html" class="navbar-link active">客户分析进阶</a>
                <a href="../projects.html" class="navbar-link">实战项目</a>
            </div>
            <button class="navbar-toggle"><i class="fas fa-bars"></i></button>
        </div>
    </nav>

    <main class="main-content">
        <section class="hero">
            <div class="hero-content">
                <div class="hero-badge">
                    <i class="fas fa-graduation-cap"></i>
                    <span>进阶课程 · 16个知识点</span>
                </div>
                <h1>{COURSE_DATA['title']}</h1>
                <p class="hero-subtitle">{COURSE_DATA['subtitle']}</p>
            </div>
        </section>

        <section class="section" style="background: var(--bg-primary);">
            <div class="container">
                <div class="section-header">
                    <span class="section-tag">Course Modules</span>
                    <h2 class="section-title">课程模块</h2>
                    <p class="section-desc">四个阶段，系统掌握客户数据分析</p>
                </div>
                <div class="modules-grid">
'''

    for module in COURSE_DATA['modules']:
        html += f'''
                    <div class="module-card" id="module-{module['id']}">
                        <div class="module-header" onclick="toggleModule({module['id']})">
                            <div class="module-info">
                                <div class="module-icon" style="background: {module['color']};">
                                    <i class="fas {module['icon']}"></i>
                                </div>
                                <div class="module-title">
                                    <h3>模块{module['id']}：{module['name']}</h3>
                                    <p>{len(module['lessons'])}个知识点</p>
                                </div>
                            </div>
                            <div class="module-meta">
                                <span class="lesson-count">{len(module['lessons'])}小节</span>
                                <i class="fas fa-chevron-down expand-icon"></i>
                            </div>
                        </div>
                        <div class="module-lessons">
                            <div class="lesson-list">
'''
        for lesson in module['lessons']:
            html += f'''
                                <a href="lesson{lesson['id']}.html" class="lesson-item">
                                    <div class="lesson-number">{lesson['id']}</div>
                                    <div class="lesson-info">
                                        <h4>{lesson['title']}</h4>
                                        <p>{lesson['desc']}</p>
                                    </div>
                                    <i class="fas fa-chevron-right lesson-arrow"></i>
                                </a>
'''
        html += '''
                            </div>
                        </div>
                    </div>
'''

    html += '''
                </div>
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="footer-content">
            <p>© 2024 数析学院 · 专注数据分析教育</p>
        </div>
    </footer>

    <script>
        function toggleModule(id) {
            document.getElementById('module-' + id).classList.toggle('open');
        }
        document.querySelector('.navbar-toggle').addEventListener('click', function() {
            document.querySelector('.navbar-menu').classList.toggle('active');
        });
    </script>
</body>
</html>'''
    return html

def create_lesson_page(module, lesson):
    """创建知识点详情页"""
    has_code = 'code' in lesson and lesson['code']

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{lesson['title']} - 客户数据分析进阶</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="../../styles.css">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        :root {{
            --primary: #1a1a2e;
            --accent: #0f3460;
            --highlight: #e94560;
            --text-primary: #2d3436;
            --text-secondary: #636e72;
            --text-muted: #b2bec3;
            --bg-primary: #ffffff;
            --bg-secondary: #f8f9fa;
            --success-bg: rgba(16, 185, 129, 0.1);
            --warning-bg: rgba(245, 158, 11, 0.1);
            --shadow-md: 0 4px 16px rgba(0,0,0,0.08);
            --radius-md: 12px;
        }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; line-height: 1.8; color: var(--text-primary); background: var(--bg-secondary); }}
        .navbar {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(255,255,255,0.95); backdrop-filter: blur(20px); border-bottom: 1px solid #e9ecef; }}
        .navbar-container {{ max-width: 1200px; margin: 0 auto; padding: 0 24px; height: 64px; display: flex; align-items: center; justify-content: space-between; }}
        .navbar-brand {{ display: flex; align-items: center; gap: 10px; font-size: 1.25rem; font-weight: 700; color: var(--primary); text-decoration: none; }}
        .navbar-brand i {{ color: var(--highlight); }}
        .navbar-menu {{ display: flex; gap: 32px; }}
        .navbar-link {{ font-size: 0.9375rem; font-weight: 500; color: var(--text-secondary); text-decoration: none; }}
        .navbar-link:hover {{ color: var(--primary); }}
        .navbar-link.active {{ color: var(--primary); font-weight: 600; }}
        .main-content {{ padding-top: 64px; }}
        .lesson-header {{ background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%); color: white; padding: 60px 24px; }}
        .lesson-header-content {{ max-width: 900px; margin: 0 auto; }}
        .breadcrumb {{ font-size: 0.875rem; opacity: 0.8; margin-bottom: 16px; }}
        .breadcrumb a {{ color: white; text-decoration: none; }}
        .breadcrumb a:hover {{ text-decoration: underline; }}
        .lesson-header h1 {{ font-size: 2rem; font-weight: 700; margin-bottom: 12px; line-height: 1.3; }}
        .lesson-header p {{ font-size: 1.125rem; opacity: 0.9; }}
        .lesson-container {{ max-width: 900px; margin: 0 auto; padding: 40px 24px; }}
        .objectives-section {{ background: var(--bg-primary); border-radius: var(--radius-md); padding: 24px; margin-bottom: 32px; box-shadow: var(--shadow-md); }}
        .objectives-section h2 {{ font-size: 1.25rem; font-weight: 600; color: var(--primary); margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }}
        .objectives-section ul {{ list-style: none; }}
        .objectives-section li {{ padding: 8px 0; padding-left: 24px; position: relative; color: var(--text-secondary); }}
        .objectives-section li::before {{ content: '✓'; position: absolute; left: 0; color: #10b981; font-weight: bold; }}
        .content-section {{ background: var(--bg-primary); border-radius: var(--radius-md); padding: 32px; margin-bottom: 32px; box-shadow: var(--shadow-md); }}
        .content-section h3 {{ font-size: 1.25rem; font-weight: 600; color: var(--primary); margin: 24px 0 16px; padding-bottom: 8px; border-bottom: 2px solid var(--bg-secondary); }}
        .content-section h3:first-child {{ margin-top: 0; }}
        .content-section p {{ margin-bottom: 16px; color: var(--text-secondary); }}
        .content-section ul, .content-section ol {{ margin: 16px 0; padding-left: 24px; color: var(--text-secondary); }}
        .content-section li {{ margin-bottom: 8px; }}
        .content-section strong {{ color: var(--text-primary); }}
        .code-section {{ background: var(--bg-primary); border-radius: var(--radius-md); padding: 24px; margin-bottom: 32px; box-shadow: var(--shadow-md); }}
        .code-section h2 {{ font-size: 1.25rem; font-weight: 600; color: var(--primary); margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }}
        .code-editor {{ background: #1e1e1e; border-radius: 8px; padding: 20px; overflow-x: auto; }}
        .code-editor pre {{ margin: 0; font-family: 'Monaco', 'Menlo', monospace; font-size: 0.875rem; line-height: 1.6; color: #d4d4d4; }}
        .code-editor .keyword {{ color: #569cd6; }}
        .code-editor .string {{ color: #ce9178; }}
        .code-editor .function {{ color: #dcdcaa; }}
        .code-editor .comment {{ color: #6a9955; }}
        .code-editor .number {{ color: #b5cea8; }}
        .tips-box {{ background: var(--success-bg); border-left: 4px solid #10b981; border-radius: 0 var(--radius-md) var(--radius-md) 0; padding: 20px 24px; margin-bottom: 24px; }}
        .tips-box h4 {{ font-size: 1rem; font-weight: 600; color: #059669; margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }}
        .tips-box p {{ color: var(--text-secondary); font-size: 0.9375rem; }}
        .errors-box {{ background: var(--warning-bg); border-left: 4px solid #f59e0b; border-radius: 0 var(--radius-md) var(--radius-md) 0; padding: 20px 24px; margin-bottom: 24px; }}
        .errors-box h4 {{ font-size: 1rem; font-weight: 600; color: #d97706; margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }}
        .errors-box p {{ color: var(--text-secondary); font-size: 0.9375rem; }}
        .footer {{ background: var(--primary); color: white; padding: 32px 24px; text-align: center; }}
        .footer p {{ opacity: 0.7; font-size: 0.875rem; }}
        @media (max-width: 768px) {{
            .lesson-header h1 {{ font-size: 1.5rem; }}
            .lesson-container {{ padding: 24px 16px; }}
            .content-section {{ padding: 20px; }}
        }}
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="navbar-container">
            <a href="../../index.html" class="navbar-brand">
                <i class="fas fa-chart-line"></i>
                <span>数析学院</span>
            </a>
            <div class="navbar-menu">
                <a href="../../index.html" class="navbar-link">首页</a>
                <a href="../customer-advanced.html" class="navbar-link">客户分析进阶</a>
                <a href="#" class="navbar-link active">{module['name']}</a>
            </div>
        </div>
    </nav>

    <main class="main-content">
        <section class="lesson-header">
            <div class="lesson-header-content">
                <div class="breadcrumb">
                    <a href="../customer-advanced.html">客户分析进阶</a> &gt; <a href="../customer-advanced.html#module-{module['id']}">{module['name']}</a> &gt; 本节
                </div>
                <h1>{lesson['title']}</h1>
                <p>{lesson['desc']}</p>
            </div>
        </section>

        <div class="lesson-container">
            <div class="objectives-section">
                <h2><i class="fas fa-bullseye"></i> 学习目标</h2>
                <ul>
'''
    for obj in lesson['objectives']:
        html += f'<li>{obj}</li>\n'

    html += '''
                </ul>
            </div>

            <div class="content-section">
'''

    # 解析HTML内容，处理代码块
    content_parts = lesson['content'].split('```')
    for i, part in enumerate(content_parts):
        if i % 2 == 0:
            # 普通内容
            html += part
        else:
            # 代码块
            html += f'''
                <div class="code-section">
                    <h2><i class="fas fa-code"></i> 代码示例</h2>
                    <div class="code-editor">
                        <pre>{part.strip()}</pre>
                    </div>
                </div>
'''

    html += f'''
            </div>

            <div class="tips-box">
                <h4><i class="fas fa-lightbulb"></i> 💡 小贴士</h4>
                <p>{lesson['tips']}</p>
            </div>

            <div class="errors-box">
                <h4><i class="fas fa-exclamation-triangle"></i> ⚠️ 常见错误</h4>
                <p>{lesson['errors']}</p>
            </div>
        </div>
    </main>

    <footer class="footer">
        <p>© 2024 数析学院 · 专注数据分析教育</p>
    </footer>
</body>
</html>'''
    return html

def main():
    import os

    # 创建课程目录
    os.makedirs(COURSE_DIR, exist_ok=True)

    # 1. 创建课程主页
    course_html = create_course_page()
    with open(os.path.join(COURSE_DIR, 'customer-advanced.html'), 'w', encoding='utf-8') as f:
        f.write(course_html)
    print(f"✓ 创建课程主页: {COURSE_DIR}/customer-advanced.html")

    # 2. 创建每个知识点的详情页
    for module in COURSE_DATA['modules']:
        for lesson in module['lessons']:
            lesson_html = create_lesson_page(module, lesson)
            with open(os.path.join(COURSE_DIR, f'lesson{lesson["id"]}.html'), 'w', encoding='utf-8') as f:
                f.write(lesson_html)
            print(f"✓ 创建知识点: lesson{lesson['id']}.html - {lesson['title']}")

    print(f"\n✅ 课程板块创建完成！共创建 1 个主页 + 16 个详情页")

if __name__ == '__main__':
    main()