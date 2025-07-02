import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Easy to Use',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        CodeWise was designed from the ground up to be easily installed and
        used to perform automatic code review and suggest improvements before approving Pull Requests.
      </>
    ),
  },
  {
    title: 'Focus on What Matters',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        CodeWise lets you focus on your project, and we&apos;ll do the code review. Go
        ahead and try it.
      </>
    ),
  },
  {
    title: 'Powered by Intelligent Code Analysis',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        CodeWise automates Pull Request reviews with smart insights, ensuring 
        code quality standards and actionable suggestions. Easily extend and 
        customize while maintaining a clear and consistent delivery structure.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
