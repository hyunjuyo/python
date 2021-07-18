from sof import get_job_infos
from save import save_to_csv

job_infos = get_job_infos()
save_to_csv(job_infos)