# -Flipkart-Mobile-Sales-Analysis
# 📱 Flipkart Mobile Sales Analysis

> **A comprehensive exploratory data analysis (EDA) of mobile phone sales data from Flipkart.**

---

## 🇮🇷 توضیحات فارسی

### درباره پروژه
این پروژه یک تحلیل اکتشافی داده (EDA) روی داده‌های فروش موبایل در پلتفرم فلیپ‌کارت هند است.  
هدف از این پروژه، بررسی رفتار مشتریان، مقایسه برندها و کشف الگوهای فروش است.

### 📊 داده‌ها
فایل داده: `Flipkart Mobile 2.csv`

| ستون | توضیح |
|------|-------|
| `brand` | برند موبایل |
| `model` | مدل موبایل |
| `base_color` | رنگ اصلی |
| `processor` | پردازنده |
| `screen_size` | سایز نمایشگر |
| `ROM` | حافظه داخلی |
| `RAM` | حافظه رم |
| `display_size` | اندازه واقعی صفحه (اینچ) |
| `num_rear_camera` | تعداد دوربین پشت |
| `num_front_camera` | تعداد دوربین جلو |
| `battery_capacity` | ظرفیت باتری |
| `ratings` | امتیاز کاربران |
| `num_of_ratings` | تعداد افرادی که رأی داده‌اند |
| `sales_price` | قیمت فروش |
| `discount_percent` | درصد تخفیف |
| `sales` | فروش کل (به صورت کرور) |

### 🔍 سؤالات تحلیل شده
- چه برندهایی در فلیپ‌کارت موجودند؟
- هر برند چند محصول دارد؟
- کدام مدل‌ها بیشترین فروش را داشتند؟
- مشتریان چه سایز صفحه‌ای را ترجیح می‌دهند؟
- محبوب‌ترین رنگ‌های موبایل کدامند؟
- کدام پردازنده‌ها بیشترین محبوبیت را دارند؟
- توزیع قیمتی موبایل‌ها چگونه است؟
- درآمد کل هر برند چقدر است؟
- میانگین تخفیف هر برند چقدر است؟

### 🛠️ ابزارها و کتابخانه‌ها
- `Python 3`
- `Pandas` — پردازش و تحلیل داده
- `NumPy` — محاسبات عددی
- `Matplotlib` — رسم نمودار
- `Seaborn` — نمودارهای آماری

---

## 🇬🇧 English Description

### About the Project
This project performs an **Exploratory Data Analysis (EDA)** on mobile phone sales data from Flipkart, one of India's largest e-commerce platforms. The goal is to uncover customer preferences, compare brand performance, and identify key sales trends.

### 📊 Dataset
File: `Flipkart Mobile 2.csv`

The dataset contains information about mobile phones listed on Flipkart, including technical specifications, pricing, ratings, and sales figures.

**Key columns:** `brand`, `model`, `base_color`, `processor`, `screen_size`, `ROM`, `RAM`, `display_size`, `num_rear_camera`, `num_front_camera`, `battery_capacity`, `ratings`, `num_of_ratings`, `sales_price`, `discount_percent`, `sales`

### 🔍 Analysis Questions Covered
- How many mobile brands are available on Flipkart?
- How many products does each brand offer?
- Which models have the highest average sales?
- What screen sizes do customers prefer most?
- What are the most popular phone colors?
- Which processors are most common?
- What price ranges do customers choose most?
- What is the total revenue generated per brand?
- What is the average discount offered per brand?

### 📈 Key Findings
- **Brand breakdown**: Samsung, Apple, Xiaomi, Realme, and Poco are the main brands analyzed.
- **Revenue**: Derived column (`revenue`) calculated as `sales × 10,000,000`.
- **Units sold**: Estimated as `revenue / sales_price`.
- **Discounts**: Analyzed per brand to understand pricing strategies.
- **Screen size preferences**: Visualized using pie charts per brand.

### 🛠️ Tech Stack

| Library | Purpose |
|---------|---------|
| `pandas` | Data loading, cleaning, grouping |
| `numpy` | Numerical operations |
| `matplotlib` | Bar charts, histograms, pie charts |
| `seaborn` | Statistical visualizations |

### 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/flipkart-mobile-analysis.git
   cd flipkart-mobile-analysis
   ```

2. **Install dependencies**
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```

3. **Add the dataset**  
   Place `Flipkart Mobile 2.csv` in the project root directory.

4. **Run the notebook**
   ```bash
   jupyter notebook Mobile.py
   ```
   > Or open `Mobile.py` as a Jupyter notebook if using VS Code with the Jupyter extension.

### 📁 Project Structure
```
flipkart-mobile-analysis/
│
├── Mobile.py               # Main analysis notebook
├── Flipkart Mobile 2.csv   # Dataset (add manually)
└── README.md               # Project documentation
```

### 📌 Notes
- The `sales` column is in **Crores** (Indian unit: 1 Crore = 10,000,000).
- `revenue` and `units_sold` are **derived columns** created during analysis.
- Some warnings may appear during execution; they do not affect results.

---

## 👤 Author

> Add your name and GitHub profile here.

---

## 📄 License

This project is for educational purposes. Dataset sourced from Flipkart public listings.
