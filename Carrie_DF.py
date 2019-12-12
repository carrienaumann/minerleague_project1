{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "data_series = \"RCPS.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>School Name</th>\n",
       "      <th># of students</th>\n",
       "      <th>Graduation Rate</th>\n",
       "      <th>Dropout rate</th>\n",
       "      <th>Absenteeism 10% or above</th>\n",
       "      <th>Funding per student</th>\n",
       "      <th>Title I</th>\n",
       "      <th>Total funding per student per state</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>Armstrong High School</td>\n",
       "      <td>849</td>\n",
       "      <td>77%</td>\n",
       "      <td>18.40%</td>\n",
       "      <td>54%</td>\n",
       "      <td>14508</td>\n",
       "      <td>100%</td>\n",
       "      <td>12548</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>Huguenot High School</td>\n",
       "      <td>1286</td>\n",
       "      <td>68.10%</td>\n",
       "      <td>30.94%</td>\n",
       "      <td>24.49%</td>\n",
       "      <td>14508</td>\n",
       "      <td>66.90%</td>\n",
       "      <td>12548</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>Thomas Jefferson High School</td>\n",
       "      <td>734</td>\n",
       "      <td>89.90%</td>\n",
       "      <td>9.52%</td>\n",
       "      <td>18.04%</td>\n",
       "      <td>14508</td>\n",
       "      <td>100%</td>\n",
       "      <td>12548</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>George Wythe High School</td>\n",
       "      <td>1121</td>\n",
       "      <td>75.60%</td>\n",
       "      <td>20.34%</td>\n",
       "      <td>46.57%</td>\n",
       "      <td>14508</td>\n",
       "      <td>100%</td>\n",
       "      <td>12548</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>John Marshall High School</td>\n",
       "      <td>667</td>\n",
       "      <td>91.80%</td>\n",
       "      <td>7.88%</td>\n",
       "      <td>34.88%</td>\n",
       "      <td>14508</td>\n",
       "      <td>67.60%</td>\n",
       "      <td>12548</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                    School Name  # of students Graduation Rate Dropout rate  \\\n",
       "0         Armstrong High School            849             77%       18.40%   \n",
       "1          Huguenot High School           1286          68.10%       30.94%   \n",
       "2  Thomas Jefferson High School            734          89.90%        9.52%   \n",
       "3      George Wythe High School           1121          75.60%       20.34%   \n",
       "4     John Marshall High School            667          91.80%        7.88%   \n",
       "\n",
       "  Absenteeism 10% or above  Funding per student Title I  \\\n",
       "0                      54%                14508    100%   \n",
       "1                   24.49%                14508  66.90%   \n",
       "2                   18.04%                14508    100%   \n",
       "3                   46.57%                14508    100%   \n",
       "4                   34.88%                14508  67.60%   \n",
       "\n",
       "   Total funding per student per state  \n",
       "0                                12548  \n",
       "1                                12548  \n",
       "2                                12548  \n",
       "3                                12548  \n",
       "4                                12548  "
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_original = pd.read_csv(data_series)\n",
    "df_original.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
