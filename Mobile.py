# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# %% [markdown]
# 🎯 ۱) اصلاً warnings چی هستند؟
# 
# warning (هشدار) =
# پیامی که پایتون نمایش می‌دهد برای اینکه:
# 
# مشکلی «کوچک» در کد وجود دارد
# 
# یا در نسخه‌های آینده رفتار این خط عوض می‌شود
# 
# یا بهتر است کد را اصلاح کنید
# 
# ⚠️ هشدار = خطا نیست
# کد متوقف نمی‌شود.

# %%
# import warnings
# warnings.filterwarnings('ignore')

# %%
df=pd.read_csv('Flipkart Mobile 2.csv')

# %%
df

# %%
df.head()

# %%
df.shape

# %%
df.head(5)


# %%
df.tail(5)

# %%
df.shape

# %%
df.size

# %%
df.info()

# %%
df.describe()

# %%
df.describe()

# %%
df.columns



# %%

df.dtypes


# %%
df.isnull().sum()


# %% [markdown]
# | ستون             | معنی                         |
# | ---------------- | ---------------------------- |
# | brand            | برند موبایل                  |
# | model            | مدل موبایل                   |
# | base_color       | رنگ اصلی                     |
# | processor        | پردازنده                     |
# | screen_size      | سایز نمایشگر                 |
# | ROM              | حافظه داخلی                  |
# | RAM              | حافظه RAM                    |
# | display_size     | اندازه واقعی صفحه (اینچ)     |
# | num_rear_camera  | تعداد دوربین پشت             |
# | num_front_camera | تعداد دوربین جلو             |
# | battery_capacity | ظرفیت باتری                  |
# | ratings          | امتیاز کاربران               |
# | num_of_ratings   | تعداد نفراتی که رای داده‌اند |
# | sales_price      | قیمت فروش                    |
# | discount_percent | درصد تخفیف                   |
# | sales            | فروش کل، به صورت Crores      |
# 

# %% [markdown]
# How many Mobile Brands are there

# %%
df["brand"].unique()

# %%
BerandDf=df.groupby('brand')
BerandDf.groups

# %%
appledf = BerandDf.get_group("Apple")
appledf.head()

# %%
PocoDf=BerandDf.get_group('Poco')
PocoDf.head()

# %%
realmedf = BerandDf.get_group("Realme")
realmedf.head()

# %%
SamsungDf=BerandDf.get_group('Samsung')
SamsungDf.head()

# %%
xiaomidf = BerandDf.get_group("Xiaomi")
xiaomidf.head()

# %% [markdown]
# How much is count for each brand ?

# %%
X1=df['brand'].value_counts()
X1

# %%
appledf['model'].value_counts()

# %%
PocoDf['model'].value_counts()

# %%
realmedf['model'].value_counts()

# %%
SamsungDf['model'].value_counts()

# %% [markdown]
# Find out uniques models for each brand

# %%
appledf['model'].unique()

# %%
appledf['model'].nunique()

# %%
PocoDf["model"].unique()

# %%
PocoDf['model'].nunique()

# %%
realmedf['model'].unique()


# %%
realmedf['model'].nunique()

# %%
SamsungDf['model'].unique()


# %%
SamsungDf['model'].nunique()

# %%
xiaomidf["model"].unique()

# %%
xiaomidf['model'].nunique()

# %%

df['revenue']=(df['sales']*10000000).round().astype(int)
df.head(5)

# %%
df['units_sold']=(df['revenue']/df['sales_price']).round().astype(int)
df.head(5)

# %%
df.units_sold.sum()

# %%
print('sales generated in crocres',df.sales.sum(),"cr")

# %%
BerandSales=BerandDf.sales.sum()
BerandSales

# %%
plt.bar(BerandSales.index,BerandSales.values)
plt.xlabel('BERANDS')
plt.ylabel('SALES in CR')
plt.show()

# %%
df['actual_discount']= df['sales_price']*df['discount_percent'] 


# %%
avg_discount=df.groupby('brand').actual_discount.mean()


# %%
plt.bar(avg_discount.index,avg_discount.values)
plt.xlabel('Brand')
plt.ylabel('Average Discount Price')
plt.show()

# %% [markdown]
# What size of display did customers like the most?
# 

# %%
screen= df.screen_size.value_counts() 
screen 

# %%
plt.pie(screen,labels=screen.index,autopct='%0.f%%',explode=[0,0,0,0.7,0.3])
plt.show()

# %%
for brand, brandDf in df.groupby('brand'):
    
    # ستون سایز صفحه برای هر برند
    brand_screen_sizes = brandDf['screen_size']

    # شمردن سایزهای صفحه
    screen_size_counts = brand_screen_sizes.value_counts()

    # رسم نمودار
    plt.pie(
        screen_size_counts,
        labels=screen_size_counts.index,
        autopct='%1.1f%%',
        startangle=90
    )

    plt.title(f'Favorite Screen Size for {brand}')
    plt.axis('equal')
    plt.show()



# %% [markdown]
# Which are the favorite colors of mobile phone customers?

# %%
Color=df['base_color'].value_counts()
Color

# %%
BerandDf['base_color'].value_counts()

# %% [markdown]
# Which processors are the most favorable for customers?

# %%
pro=df['processor'].value_counts()
pro

# %%
plt.bar(pro.index,pro)
plt.xlabel('Processor')
plt.ylabel('Count')
plt.show()


# %%
BerandDf.processor.value_counts()

# %% [markdown]
# . Find out mobile phones at various price ranges. which budget range do customerschoose mostly?

# %%
df.columns

# %%
plt.figure(figsize=(8,5))

plt.hist(
    df.sales_price,
    bins=10,          # خودش bins‌ رو مرتب می‌سازه
    edgecolor="black" # مرزبندی واضح
)

plt.xlabel("Sales Price")
plt.ylabel("Frequency")
plt.title("Histogram of Sales Price")
plt.tight_layout()
plt.show()




# %% [markdown]
# Which are the top 10 models by avg sales
# 
# 
# 

# %%
avg_sales_by_model=df.groupby('model')['sales'].mean()
avg_sales_by_model

# %%
Top10Model=avg_sales_by_model.sort_values(ascending=False).head(10)
Top10Model

# %%
Top10Model.plot(kind='bar')
plt.xlabel('Models')
plt.ylabel('Sales in Crore')
for i, value in enumerate(Top10Model): 
    plt.text(i, value, str(round(value, 2)), ha='center', va='bottom') 
 
plt.tight_layout() 
plt.show() 
                

# %% [markdown]
# What is Battery capacity by brand

# %%

BerandDf.battery_capacity.value_counts()


